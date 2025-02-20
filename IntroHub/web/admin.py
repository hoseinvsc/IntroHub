from django.contrib import admin
from .models import Product

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']