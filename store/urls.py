from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    root_redirect, home, register,
    product_list, product_detail,
    cart, add_to_cart, remove_from_cart,
    logout_view, login_view, OrderCreateAPIView, OrderListAPIView, OrderViewSet
)
from . import views
router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', root_redirect, name='root'),
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('api/orders/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('api/orders/', OrderListAPIView.as_view(), name='order-list'),
    path('api/', include(router.urls)),
    path('create-payment-intent/', views.create_payment_intent, name='create_payment_intent'),
    path('stripe-webhook/', views.stripe_webhook, name='stripe_webhook'),
    path('payment-success/', views.payment_success, name='payment_success'),
]



