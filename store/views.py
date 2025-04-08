from django.shortcuts import render, get_object_or_404
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer

<<<<<<< HEAD

=======
# Веб-бет функциялары
>>>>>>> 94493687e42e90773dd67b5e2f82416f3a921731
def home(request):
    return render(request, 'store/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def cart(request):
    return render(request, 'store/cart.html')

<<<<<<< HEAD

=======
# DRF API viewset
>>>>>>> 94493687e42e90773dd67b5e2f82416f3a921731
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




