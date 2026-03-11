from django.contrib import admin
from .models import Product, Category

# Register models Product and Category
admin.site.register(Product)
admin.site.register(Category)