from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from rave_python import Rave, RaveExceptions
from store.models import Product
from order.models import Order, orderItem
from .forms import PaymentForm 
from .encoder import PythonObjectEncoder
from json import dumps, loads, JSONEncoder, JSONDecoder
import pickle
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
        amount = order.get_total_cost()
        rave = Rave(shop.public_key, shop.secret_key, usingEnv=False)

        form = PaymentForm(self.request.POST)
        
        if form.is_valid():
            cc = form.cleaned_data
            network = str(cc['network'])
            email = str(order.email)
            phonenumber = str(cc["phone_number"])
            print(phonenumber)
            payload = {
                "amount" : amount,
                "network": network,
                "email": email,
                "phonenumber": phonenumber,
                "IP": '',
                "redirect_url": "https://rave-webhook.herokuapp.com/receivepayment"
            } 

            try:

                response = loads(rave.GhMobile.charge(payload), cls=PythonObjectEncoder)

            except RaveExceptions.TransactionChargeError as e:
                print(e.err['errMsg'])
        

        return render(self.request, self.template)