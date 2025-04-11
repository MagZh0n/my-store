from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock')  
    search_fields = ('name',) 
    list_filter = ('price',) 

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_price')
    list_filter = ('created_at',)
