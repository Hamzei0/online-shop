from django.views import generic

from .models import Product
from .forms import CommentForm


class ProductsListView(generic.ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'    
    
    
class ProductsDetailView(generic.DetailView):
    model = Product
    template_name = 'products/products_detail.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        return context
    
    
    