from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home, product_list, product_detail, cart, ProductViewSet

<<<<<<< HEAD

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    
=======
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
>>>>>>> 94493687e42e90773dd67b5e2f82416f3a921731
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),
<<<<<<< HEAD

 
=======
>>>>>>> 94493687e42e90773dd67b5e2f82416f3a921731
    path('api/', include(router.urls)),  
]
