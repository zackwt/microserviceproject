from django.contrib import admin
from .models import Product, Order, OrderItem, Cart, CartItem, Payment, Shipping, Review

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Payment)
admin.site.register(Shipping)
admin.site.register(Review)