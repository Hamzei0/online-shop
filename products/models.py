from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager,self).get_queryset().filter(active=True)


class Product(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=100)
    short_description = models.CharField(
        verbose_name=_('short description'),
        max_length=300,
        blank=True
        )
    description = RichTextField(verbose_name=_('description'),)
    price = models.PositiveIntegerField(verbose_name=_('price'), default=0)
    active = models.BooleanField(verbose_name=_('active'), default=True)
    
    cover = models.ImageField(verbose_name=_('image'), upload_to='product/product_cover', blank=True)
    
    datetime_created = models.DateTimeField(verbose_name=_('datetime_created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(verbose_name=_('datetime_modified'), auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])
    

class CommentProduct(models.Model):
    PRODUCT_STARS = [
        ('1',_('very bad')),
        ('2',_('bad')),
        ('3',_('normal')),
        ('4',_('good')),
        ('5',_('perfect')),
    ]
    
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='comments',
        verbose_name=_('product name')
        )
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        related_name='comments',
        verbose_name=_('comment author')
        )
    
    text = models.TextField(verbose_name=_('comment text'))
    active = models.BooleanField(default=False, verbose_name=_('active'))
    stars = models.CharField(
        max_length=10, 
        choices=PRODUCT_STARS,
        verbose_name=_('comment stars'),
        )
    

    datetime_created = models.DateTimeField(auto_now_add=True , verbose_name=_('datetime created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime modified'))
    
    # manager
    objects = models.Manager()
    comment_filter = ActiveManager()
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
    
    
