from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from rave_python import Rave, RaveExceptions
from store.models import Product
from order.models import Order, orderItem
from .forms import PaymentForm 


import pickle
import requests
# Create your views here.


class PaymentProcess(View):
    template  = 'payment_process.html'

    def get(self, *args, **kwargs):
        form = PaymentForm()
        context = {
            "form": form
        }
        return render(self.request, self.template, context)

    def get_object(self):
        order_id = self.kwargs.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        return order

    def post(self, *args, **kwargs):
        order = self.get_object()
        order_item  = orderItem.objects.get(order=order)
        product = order_item.product
        shop = product.shop
        secret_key = str(shop.secret_key)
        amount = str(order.get_total_cost())
        print(secret_key)

        form = PaymentForm(self.request.POST)
        
        if form.is_valid():
            cc = form.cleaned_data
            network = str(cc['network'])
            email = str(order.email)
            phonenumber = str(cc["phone_number"])
            print(phonenumber)
            payload = {
               "amount": amount ,
               "email": email ,
               "currency": 'GHS',
               "mobile_money": {
                   "phone": "0551234987",
                   "provider": 'mtn' 
               }
            } 
            headers = {
                "Authorization": "Bearer" + " " + secret_key,
                "Content-Type": "application/json"

            }

            url = "https://api.paystack.co/charge"
            response = requests.post(url, json=payload, headers=headers)
            print(response.content)

            

        return render(self.request, self.template)