from django.contrib import admin
from .models import Product,ProductImage,Category,Customer,Blog

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']



admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Blog)