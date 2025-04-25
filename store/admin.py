from django.contrib import admin
from .models import Product, ProductImage
<<<<<<< HEAD
from django.contrib import admin
from .models import Product, Order, OrderItem 

admin.site.register(Order)
admin.site.register(OrderItem)
=======
>>>>>>> 8d5f8d7910a12b75e7a02703ef9d53d361302d3d

class ProductImageInline(admin.TabularInline):  
    model = ProductImage
    extra = 1  

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]  #
    list_display = ('name', 'price', 'description')  

admin.site.register(Product, ProductAdmin)

