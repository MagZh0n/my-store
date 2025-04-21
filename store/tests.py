from django.test import TestCase
<<<<<<< HEAD
from django.contrib.auth.models import User
from .models import Product, Order, Cart, CartItem, OrderItem

class ProductModelTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.99,
            stock=100
        )
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 10.99)
        self.assertEqual(product.stock, 100)

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_create_order(self):
        order = Order.objects.create(user=self.user, total_price=50.00)
        self.assertEqual(order.user.username, 'testuser')
        self.assertEqual(order.total_price, 50.00)

class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser')
        self.product = Product.objects.create(name='Product A', description='desc', price=20.0, stock=5)

    def test_create_cart_and_cart_item(self):
        cart = Cart.objects.create(user=self.user)ы
        item = CartItem.objects.create(cart=cart, product=self.product, quantity=2)
        self.assertEqual(cart.user.username, 'testuser')
        self.assertEqual(item.quantity, 2)
ы
class OrderItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser')
        self.product = Product.objects.create(name='Product A', description='desc', price=30.0, stock=10)
        self.order = Order.objects.create(user=self.user, total_price=60.0)

    def test_create_order_item(self):
        item = OrderItem.objects.create(order=self.order, product=self.product, quantity=2, price=30.0)
        self.assertEqual(item.quantity, 2)
        self.assertEqual(item.product.name, 'Product A')
        self.assertEqual(item.price, 30.0)
=======

# Create your tests here.
>>>>>>> 4f2ffa29df2bc500bfeb6c0429918f23ef1ca856
