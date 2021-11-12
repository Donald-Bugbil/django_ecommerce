from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Shop
from .models import Product
from cart.forms import Quantity_select_form

# Create your views here.

class Store(View):
    template_name = 'store.html'

    def get_query_set(self):
        shops = Shop.objects.all()
        return shops

    def get(self,request, *args,  **kwargs):
        context ={
            'shops': self.get_query_set()
        }
        return render(request, self.template_name, context)
    

class detail_store(View):
    template_name = 'detail_store.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        store = get_object_or_404(Shop, slug=slug)
        return store 

    def get(self, request, *args, **kwargs ):
        context = {'store': self.get_object()}
        return render(request, self.template_name, context)
    
class product_detail(View):
    template_name = 'product_detail.html'
 
    def get_object(self):
        slug = self.kwargs['slug']
        product = get_object_or_404(Product, slug=slug)
        return product
    
    def get(self, request, *args, **kwargs):
        form = Quantity_select_form()
        context = {
            'product': self.get_object(), 
            'shop': self.get_object().shop, 
            'Quantity_select_form' : form
        }
        return render(request, self.template_name, context)


   



    