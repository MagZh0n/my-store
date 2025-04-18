from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Order, OrderItem, CartItem  # Добавлен импорт Order
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import OrderCreateSerializer, OrderSerializer  # Добавлен импорт OrderSerializer
from rest_framework import generics


def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('home')
    return redirect('register')

@login_required
def home(request):
    return render(request, 'store/home.html')

@login_required
def logout_view(request):
    auth_logout(request)
    messages.success(request, "Вы успешно вышли из системы")
    return redirect('home')

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

@login_required
def cart(request):
    cart_items = request.session.get('cart', [])
    products_in_cart = []
    total_sum = 0

    for item in cart_items:
        product = get_object_or_404(Product, id=item['product_id'])
        item_total = product.price * item['quantity']
        total_sum += item_total
        products_in_cart.append({
            'product': product,
            'quantity': item['quantity'],
            'item_total': item_total
        })
    
    return render(request, 'store/cart.html', {
        'cart_items': products_in_cart,
        'total_sum': total_sum
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', [])

    for item in cart:
        if item['product_id'] == product.id:
            item['quantity'] += 1
            break
    else:
        cart.append({'product_id': product.id, 'quantity': 1})

    request.session['cart'] = cart
    return redirect('cart')

@login_required
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    cart = [item for item in cart if item['product_id'] != product_id]
    request.session['cart'] = cart
    return redirect('cart')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Вы успешно вошли")
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'store/login.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'store/register.html', {'form': form})

class OrderCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            order = serializer.save()
            return Response({"message": "Заказ оформлен успешно!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
