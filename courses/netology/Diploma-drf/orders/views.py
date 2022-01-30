from django.core.mail import send_mail
from django.db import IntegrityError
from django.db.models import Q, Sum, Prefetch
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ujson import loads as load_json

from backendAPI.models import Product
from orders.models import OrderItem, Order
from orders.serializers import OrderSerializer, OrderItemAddSerializer
from users.models import User, Contact


class ProviderOrders(APIView):
    print('вызов заказа')
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        (поставщик) - получить заказы
        """
        if request.user.type != 'shop':
            return Response({'status': False, 'error': 'Только для магазинов'}, status=status.HTTP_403_FORBIDDEN)

        pr = Prefetch('ordered_items', queryset=OrderItem.objects.filter(shop__user_id=request.user.id))
        order = Order.objects.filter(
            ordered_items__shop__user_id=request.user.id).exclude(status='cart') \
            .prefetch_related(pr).select_related('contact').annotate(
            total_sum=Sum('ordered_items__total_amount'),
            total_quantity=Sum('ordered_items__quantity'))
        print(pr, order.all())

        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        (пользователь) - просмотреть корзину
        """
        cart = Order.objects.filter(
            user_id=request.user.id, status='cart').prefetch_related(
            'ordered_items').annotate(
            total_sum=Sum('ordered_items__total_amount'),
            total_quantity=Sum('ordered_items__quantity'))

        serializer = OrderSerializer(cart, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        (пользователь) - добавить товар в корзину
        """
        items = request.data.get('items')
        if items:
            try:
                items_dict = load_json(items)
            except ValueError:
                Response({'Status': False, 'Errors': 'Неверный формат запроса'})
            else:
                cart, _ = Order.objects.get_or_create(user_id=request.user.id, status='cart')
                objects_created = 0
                for order_item in items_dict:
                    order_item.update({'order': cart.id})
                    product = Product.objects.filter(external_id=order_item['external_id']).values('category', 'shop',
                                                                                                   'name', 'price')
                    order_item.update({'category': product[0]['category'], 'shop': product[0]['shop'],
                                       'product_name': product[0]['name'], 'price': product[0]['price']})
                    serializer = OrderItemAddSerializer(data=order_item)
                    if serializer.is_valid():
                        try:
                            serializer.save()
                        except IntegrityError as error:
                            return Response({'status': False, 'errors': str(error)},
                                            status=status.HTTP_400_BAD_REQUEST)
                        else:
                            objects_created += 1
                    else:
                        return Response({'status': False, 'error': serializer.errors},
                                        status=status.HTTP_400_BAD_REQUEST)
                return Response({'status': True, 'num_objects': objects_created})

        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        """
        (пользователь) - изменить колличество товара
        """
        items = request.data.get('items')
        if items:
            try:
                items_dict = load_json(items)
            except ValueError:
                Response({'Status': False, 'Errors': 'Неверный формат запроса'})
            else:
                cart, _ = Order.objects.get_or_create(user_id=request.user.id, status='cart')
                objects_updated = 0
                for order_item in items_dict:
                    if isinstance(order_item['id'], int) and isinstance(order_item['quantity'], int):
                        objects_updated += OrderItem.objects.filter(order_id=cart.id, id=order_item['id']).update(
                            quantity=order_item['quantity'])

                return Response({'status': True, 'edit_objects': objects_updated})
        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        (пользователь) - удалить товар из корзины
        """
        items = request.data.get('items')
        if items:
            items_list = items.split(',')
            cart, _ = Order.objects.get_or_create(user_id=request.user.id, status='cart')
            query = Q()
            objects_deleted = False
            for order_item_id in items_list:
                if order_item_id.isdigit():
                    query = query | Q(order_id=cart.id, id=order_item_id)
                    objects_deleted = True

            if objects_deleted:
                deleted_count = OrderItem.objects.filter(query).delete()[0]
                return Response({'status': True, 'del_objects': deleted_count}, status=status.HTTP_204_NO_CONTENT)
        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)


class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        пользователь - (сформировать заказ)
        """
        order = Order.objects.filter(
            user_id=request.user.id).exclude(status='cart').select_related('contact').prefetch_related(
            'ordered_items').annotate(
            total_quantity=Sum('ordered_items__quantity'),
            total_sum=Sum('ordered_items__total_amount')).distinct()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'Status': False, 'Error': 'Log in required'}, status=403)

        if {'id', 'contact'}.issubset(request.data):
            if request.data['id'].isdigit():
                try:
                    is_updated = Order.objects.filter(
                        user_id=request.user.id, id=request.data['id']).update(
                        contact_id=request.data['contact'],
                        status='new')
                except IntegrityError as error:
                    print(error)
                    return Response({'Status': False, 'Errors': 'Неправильно указаны аргументы'})
                else:
                    if is_updated:
                        message_email, customer_email = to_place_an_order(request)
                        send_mail('Получен новый заказ ', message_email,
                                  'drf-diploma@mail.ru', [customer_email], fail_silently=False)

                        return Response({'Status': True})

        return Response({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


def to_place_an_order(request):
    """
    Функция обрабатывает реквест, и поддтягивая данные из БД формирует текстовое представления заказа
    Возвращает детали заказа текстом, и email покупателя.
    """
    order_ = Order.objects.get(user_id=request.user)
    text_order = 'Номер заказа: ' + str(order_)
    order_id_ = order_.pk
    order_detail_ = tuple(OrderItem.objects.filter(order_id=order_id_))
    total_amount = 0
    for i in order_detail_:
        text_order += ('\n' + str(i.product_name) + ' - ' + str(i.quantity) + ' шт.   -   ' + str(i.price) + ' рублей')
        total_amount += i.total_amount
    text_order += '\nСумма заказа: ' + str(total_amount)
    text_order += '\nАдрес доставки: ' + str(Contact.objects.get(user_id=request.user))
    customer_email = User.objects.get(pk=request.user.pk).email

    return text_order, customer_email
