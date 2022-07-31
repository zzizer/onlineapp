from django.contrib import admin
from .models import Product, Category, Saler

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'category_name')

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Saler)
