from distutils.util import strtobool

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db.models import Q
from requests import get
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from yaml import load as load_yaml, Loader

from .models import Shop, Category, Product, ProductParameter, Parameter
from .serializers import ShopSerializer, CategorySerializer, ProductSerializer


class ProviderUpdate(APIView):
    """
    (поставщик) - обновить прайс
    """
    permission_classes = [IsAuthenticated]
    throttle_scope = 'change_price'

    def post(self, request, *args, **kwargs):
        if request.user.type != 'shop':
            return Response({'status': False, 'error': 'Только для магазинов'}, status=status.HTTP_403_FORBIDDEN)

        url = request.data.get('url')
        print(url)
        if url:
            validate_url = URLValidator()
            try:
                validate_url(url)
            except ValidationError as e:
                return Response({'status': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                stream = get(url).content

                data = load_yaml(stream, Loader=Loader)
                print(f'{request.user.id=}')

                shop, _ = Shop.objects.get_or_create(user_id=request.user.id,
                                                     defaults={'name': data['shop'], 'url': url})
                for category in data['categories']:
                    category_object, _ = Category.objects.get_or_create(id=category['id'], name=category['name'])
                    category_object.shops.add(shop.id)
                    category_object.save()

                print(Product.objects.filter(shop_id=shop.id))

                for item in data['goods']:
                    category_ = Category.objects.get(pk=item['category'])
                    product_ = Product.objects.create(
                        name=item['name'],
                        external_id=item['id'],
                        category=category_,
                        model=item['model'],
                        price=item['price'],
                        price_rrc=item['price_rrc'],
                        quantity=item['quantity'],
                        shop_id=shop.id)
                    for name, value in item['parameters'].items():
                        parameter_id_, _ = Parameter.objects.get_or_create(name=name)
                        ProductParameter.objects.create(
                            product_id=product_.pk,
                            parameter_id=parameter_id_.pk,
                            value=value)

                if shop.name != data['shop']:
                    return Response({'status': False, 'error': 'В файле указано некорректное название магазина!'},
                                    status=status.HTTP_400_BAD_REQUEST)

                return Response({'status': True})

        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)


class ProviderState(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        получить статуса магазина
        """
        if request.user.type != 'shop':
            return Response({'status': False, 'error': 'Только для магазинов'}, status=status.HTTP_403_FORBIDDEN)

        shop = request.user.shop
        serializer = ShopSerializer(shop)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        изменить статус магазина
        """
        if request.user.type != 'shop':
            return Response({'status': False, 'error': 'Только для магазинов'}, status=status.HTTP_403_FORBIDDEN)

        state = request.data.get('state')
        if state:
            try:
                Shop.objects.filter(user_id=request.user.id).update(state=strtobool(state))
                return Response({'status': True})
            except ValueError as error:
                return Response({'status': False, 'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'status': False, 'error': 'Не указано поле "Статус".'}, status=status.HTTP_400_BAD_REQUEST)


class ShopViewSet(viewsets.ModelViewSet):
    """
    просмотр списка магазинов
    """
    queryset = Shop.objects.filter(state=True)
    serializer_class = ShopSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    просмотр категорий
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(APIView):
    """
    поиск всех или определеных товаров
    """

    def get(self, request, *args, **kwargs):

        query = Q(shop__state=True)
        shop_id = request.query_params.get('shop_id')
        category_id = request.query_params.get('category_id')

        if shop_id:
            query = query & Q(shop_id=shop_id)

        if category_id:
            query = query & Q(category_id=category_id)

        queryset = Product.objects.filter(
            query).select_related(
            'shop', 'category').prefetch_related(
            'product_parameters').distinct()

        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)
