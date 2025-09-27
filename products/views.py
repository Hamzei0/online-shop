from django.views import generic
from django.shortcuts import reverse , get_object_or_404

from .models import Product, CommentProduct
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


class CommentCreateView(generic.CreateView):
    model = CommentProduct
    form_class = CommentForm
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product
        
        return super().form_valid(form)

    