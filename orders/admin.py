from django.contrib import admin
from . import models

class OrderItemInLine(admin.TabularInline):
    model = models.OrderItem
    fields = ['order','product','quantity','price']
    extra = 1

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','last_name','datetime_created','is_paid']
    
    inlines = [
        OrderItemInLine,
    ]


@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','product','quantity','price']
    