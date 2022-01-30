from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ConfirmEmailToken, Contact, User
from .serializers import UserSerializer, ContactSerializer


class RegisterUser(APIView):
    """
    регистрация пользователя
    """
    throttle_scope = 'register'

    def post(self, request, *args, **kwargs):
        if {'first_name', 'last_name', 'email', 'password', 'company', 'position'}.issubset(request.data):
            try:
                validate_password(request.data['password'])
            except Exception as password_error:
                return Response({'status': False, 'error': {'password': password_error}},
                                status=status.HTTP_403_FORBIDDEN)
            else:
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():
                    user = user_serializer.save()
                    user.set_password(request.data['password'])
                    user.save()
                    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user.id)
                    return Response({'status': True, 'token for confirm email': token.key})
                else:
                    return Response({'status': False, 'error': user_serializer.errors},
                                    status=status.HTTP_403_FORBIDDEN)
        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)


class ConfirmAccount(APIView):
    """
    подтверждение регистрации
    """

    # Регистрация методом POST
    def post(self, request, *args, **kwargs):
        if {'email', 'token'}.issubset(request.data):

            token = ConfirmEmailToken.objects.filter(user__email=request.data['email'],
                                                     key=request.data['token']).first()
            if token:
                token.user.is_active = True
                token.user.save()
                token.delete()
                return Response({'Status': True})
            else:
                return Response({'Status': False, 'Errors': 'Неправильно указан токен или email'})

        return Response({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class LoginUser(APIView):
    """
    авторизация - получение токена
    """

    def post(self, request, *args, **kwargs):
        if {'email', 'password'}.issubset(request.data):
            user = authenticate(request, username=request.data['email'], password=request.data['password'])
            if user is not None:
                if user.is_active:
                    token, _ = Token.objects.get_or_create(user=user)

                    return Response({'status': True, 'token': token.key})

            return Response({'status': False, 'error': 'Не удалось войти'}, status=status.HTTP_403_FORBIDDEN)

        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        (пользователь) - получить данные пользователя
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        (пользователь) - изменить данные пользователя
        """
        if {'password'}.issubset(request.data):
            if 'password' in request.data:
                try:
                    validate_password(request.data['password'])
                except Exception as password_error:
                    return Response({'status': False, 'error': {'password': password_error}},
                                    status=status.HTTP_400_BAD_REQUEST)
                else:
                    request.user.set_password(request.data['password'])

            user_serializer = UserSerializer(request.user, data=request.data, partial=True)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({'status': True}, status=status.HTTP_200_OK)
            else:
                return Response({'status': False, 'error': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Status': False, 'Errors': 'Не указаны все необходимые аргументы(Password)'})


class ContactView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        (пользователь) - получить контакты
        """
        contact = Contact.objects.filter(user__id=request.user.id)
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        (пользователь) - добавить контакт
        """
        if {'city', 'street', 'phone'}.issubset(request.data):
            request.data._mutable = True
            request.data.update({'user': request.user.id})
            serializer = ContactSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'status': True}, status=status.HTTP_201_CREATED)
            else:
                Response({'status': False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        """
        (пользователь) - изменить контакт
        """
        if {'id'}.issubset(request.data):
            try:
                contact = Contact.objects.get(pk=int(request.data["id"]))
            except ValueError:
                return Response(
                    {'status': False, 'error': 'Неверный тип поля ID.'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = ContactSerializer(contact, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True}, status=status.HTTP_200_OK)
            return Response({'status': False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        (пользователь) - удалить контакт
        """
        if {'items'}.issubset(request.data):
            for item in request.data["items"].split(','):
                try:
                    contact = Contact.objects.get(pk=int(item))
                    contact.delete()
                except ValueError:
                    return Response({'status': False, 'error': 'Неверный тип поля (items).'},
                                    status=status.HTTP_400_BAD_REQUEST)

            return Response({'status': True}, status=status.HTTP_204_NO_CONTENT)

        return Response({'status': False, 'error': 'Не указаны ID контактов'},
                        status=status.HTTP_400_BAD_REQUEST)


def home(request):
    return render(request, 'home.html')

def verify(request, uuid):
    try:
        user = User.objects.get(verification_uuid=uuid, is_verified=False)
    except User.DoesNotExist:
        raise Http404('Пользователя не существует, или он уже подтверждён')

    user.is_verified = True
    user.save()

    return redirect('home')