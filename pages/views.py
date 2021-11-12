from django.shortcuts import render

from django.views.generic import View
from django.views.generic.base import ContextMixin
from store.models import Shop, Category, Product

# Create your views here.

class HomePage(View):
    template_name = 'home.html'
    
    def get_apparels_queryet(self):
        category = Category.objects.get(name_of_category='apparels')  
        products = Product.objects.filter(category=category)    
        return products

    #def get_food_queryset(self):
     #   category = Category.objects.get(name_of_category='food')
      #  products = Product.objects.filter(category='category')
       # return products

    def get_query_set(self):
        shops = Shop.objects.all()
        return shops
   
    
    def get(self, request, *args, **kwargs):
        context ={'apparels': self.get_apparels_queryet(), 'shops': self.get_query_set()}
        return render(request, self.template_name, context)
    
  

    


