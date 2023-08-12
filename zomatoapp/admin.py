from django.contrib import admin
from .models import Dish, Order, OrderItem

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('dish_name', 'price', 'availability','image_url')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'status')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'dish', 'quantity')
