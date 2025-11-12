from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name=_('is paid'), default=False)
    
    first_name = models.CharField(verbose_name=_('first name'), max_length=70)
    last_name = models.CharField(verbose_name=_('last name'), max_length=70)
    
    phone_number = models.CharField(verbose_name=_('phone number'), max_length=15)
    address = models.CharField(verbose_name=_('address'), max_length=700)
    order_notes = models.TextField(verbose_name=_('order_notes'), blank=True)
    
    datetime_created = models.DateTimeField(verbose_name=_('datetime_created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(verbose_name=_('datetime_modified'), auto_now=True)
    
    def __str__(self):
        return f'Order: {self.id}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE , related_name='item')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE , related_name='order_items')
    quantity = models.PositiveIntegerField(default=1) 
    price = models.PositiveIntegerField() 
    
    def __str__(self):
        return f'Order Item: {self.id}: {self.product} x {self.quantity} (price: {self.price})'
    