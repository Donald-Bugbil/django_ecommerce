from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .forms import OrderCreationForm
from cart.cart import Cart
from .models import orderItem
from django.urls import reverse
from store.models import Product
from django.http import HttpResponseRedirect
import simplejson as json
from django.core.serializers import serialize



# Create your views here.


class OrderCreate(View):
    template = 'ordercreate.html'

    def get(self, *args, **kwargs):
        cart = Cart(self.request)
        product = self.get_object()
        for item in cart:
            if item['product'].id == product.id:
                cart_item = item

        context = {
            'form': OrderCreationForm(),
            'cart': cart,
            'item': cart_item
        }
        print(cart_item)

        return render(self.request, self.template, context)

    def get_object(self):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        return product

    def post(self, *args, **kwargs):
        cart = Cart(self.request)
        product = self.get_object()
        for item in cart:
            if item['product'].id == product.id:
                cart_item = item
        price = cart_item['price']
        form = OrderCreationForm(self.request.POST)
        if form.is_valid():
            order = form.save()
            orderItem.objects.create(
                order=order,
                product=cart_item['product'],
                price=cart_item['price'],
                quantity=cart_item['quantity']
            )
            serial_object = serialize('json', [ product, ])
        
            cart.Delete(serial_object)
            return HttpResponseRedirect(reverse('payment:paymentprocess', kwargs={'order_id': order.id}))
            context = {
                "form": form,
            }

        return render(self.request, self.template, context)
