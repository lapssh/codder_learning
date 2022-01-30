from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders.views import CartView, OrderView, ProviderOrders
from .views import ProviderUpdate, ProductView, ProviderState, ShopViewSet, CategoryViewSet

app_name = 'backendAPI'

router = DefaultRouter()
router.register(r'shops', ShopViewSet)
router.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('user/', include('users.urls', namespace='users')),
    path('products', ProductView.as_view(), name='products'),
    path('partner/update', ProviderUpdate.as_view(), name='partner-update'),
    path('partner/state/', ProviderState.as_view(), name='partner-state'),
    path('partner/orders', ProviderOrders.as_view(), name='partner-shopAPI'),
    path('cart', CartView.as_view(), name='cart'),
    path('order', OrderView.as_view(), name='order'),
]

urlpatterns += router.urls
