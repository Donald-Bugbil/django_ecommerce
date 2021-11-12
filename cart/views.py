from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from store.models import Product
from .forms import Quantity_select_form
from .cart import Cart
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST 
from .forms import Quantity_select_form
from django.urls import reverse


# Create your views here.
@method_decorator(require_POST, name='dispatch')
class Add_to_cart(View):

    def get_object(self):
        id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=id)
        return product 

    def post(self, *args, **kwargs):
        cart = Cart(self.request)
        form = Quantity_select_form(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=self.get_object(), quantity=cd['quantity'], override_quantity=cd['override'])
        return redirect(reverse('cart:cart_detail'))
        
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
             

@method_decorator(require_POST, name='dispatch')    
class Remove(View):

    def get_object(self):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id = product_id)
        return product
    
    def post(self, *args, **kwargs):
        cart = Cart(self.request)
        cart.remove(self.get_object())
        return redirect('cart:cart_detail')

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class Cart_detail(View):
    template_name = 'cart_detail.html'

    def get(self, *args, **kwargs):
        form = Quantity_select_form()
        cart = Cart(self.request)
        context = {
            'cart': cart,
            'form': form
        }
        return render(self.request, self.template_name, context)
    



        
