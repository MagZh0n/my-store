from django.urls import path
from .views import (
    root_redirect, home, register,
    product_list, product_detail,
    cart, add_to_cart, remove_from_cart,
    logout_view, login_view, OrderCreateAPIView, OrderListAPIView
)


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
]



