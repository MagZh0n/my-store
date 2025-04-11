from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem
from django.http import HttpResponse

def home(request):
    return render(request, 'store/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def cart(request):
    cart_items = request.session.get('cart', [])
    products_in_cart = []

    for item in cart_items:
        product = get_object_or_404(Product, id=item['product_id'])
        products_in_cart.append({'product': product, 'quantity': item['quantity']})

    return render(request, 'store/cart.html', {'cart_items': products_in_cart})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', [])

    item_found = False
    for item in cart:
        if item['product_id'] == product.id:
            item['quantity'] += 1
            item_found = True
            break

    if not item_found:
        cart.append({'product_id': product.id, 'quantity': 1})

    request.session['cart'] = cart

    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    cart = [item for item in cart if item['product_id'] != product_id]
    request.session['cart'] = cart
    return redirect('cart')






