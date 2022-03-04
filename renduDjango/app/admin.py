from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price', 'image', 'quantity']


admin.site.register(Product)
