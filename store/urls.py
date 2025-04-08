from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home, product_list, product_detail, cart, ProductViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),

 
    path('api/', include(router.urls)),  
]
