from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='products_list'),
    path('<int:pk>', views.ProductsDetailView.as_view(), name='products_detail'),
    path('comment/<int:product_id>', views.CommentCreateView.as_view(), name='comment_create'),
]
