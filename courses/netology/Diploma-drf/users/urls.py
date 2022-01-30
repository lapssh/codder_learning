from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from .views import RegisterUser, LoginUser, UserDetails, ContactView, ConfirmAccount

app_name = 'users'

urlpatterns = [
    path('register', RegisterUser.as_view(), name='user-register'),
    path('register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('login', LoginUser.as_view(), name='user-login'),
    path('contact', ContactView.as_view(), name='user-contact'),
    path('details', UserDetails.as_view(), name='user-details'),
    path('password_reset', reset_password_request_token, name='password-reset'),
    path('password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
]
