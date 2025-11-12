from django.urls import path

from . import views

urlpatterns = [
    path('product_list/', views.ProductList.as_view(), name='product_list'),
    path('<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('comment/<int:product_id>/', views.CommentCreate.as_view(), name='comment_create'),
]