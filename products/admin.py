from django.contrib import admin

from .models import Product,CommentProduct

@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title','price','active']


@admin.register(CommentProduct)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product','author','stars','active']
    
    
    