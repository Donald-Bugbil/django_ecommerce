import pytest 
from django.test import RequestFactory as rf
pytestmark = pytest.mark.django_db
from pytest_django.asserts import assertContains
from django.urls import reverse 
from .factories import (
    ShopCategoryFactory,
    ProductFactory,
    CategoryFactory,
    DeliveryPersonFactory,
    ShopFactory

)
from .views import (
    Store,
    detail_store,
    product_detail

)

# Test for the list of stores
def test_store_list(rf):
    #url for the store view 
    url = reverse('store:store') 

     # getting the request object
    request = rf.get(url) 

    # views are functions but you can write them in classes and calling  
    # as_view() on it
    callable_object = Store.as_view() 

    # the request is then passed as an argument to the callable object or view 
    # to form the response object
    response = callable_object(request)

    assertContains(response, status_code =200, text='Shops')

# Test for store detail page
def test_store_detail(rf):
    # creating a new category object
    category = ShopCategoryFactory()

    # creating a new shop object
    shop = ShopFactory(category=category)

    # url for the detail store page and passing the slug as a url argument
    url = reverse('store:detail_store', kwargs={'slug': shop.slug})

    # getting the request object 
    request = rf.get(url)

    # views are functions but you can write them in classes and calling  
    # as_view() on it
    callable_object = detail_store.as_view()

    # the request is then passed as an argument to the callable object or view 
    # to form the response object
    response = callable_object(request, slug=shop.slug)

    assertContains(response, shop.name)

# test for product detail page 
def test_product_detail(rf):
    # an instance of a shop category
    shop_category = ShopCategoryFactory()

    # an instance of a shop
    shop = ShopFactory(category=shop_category)

    # an instance of a category object
    category = CategoryFactory()

    # creating a new product
    product = ProductFactory(shop=shop, category=category)

    # getting the url 
    url = reverse('store:productdetail', kwargs={'slug': product.slug})

    # getting the request object 
    request = rf.get(url)

     # views are functions but you can write them in classes and calling  
    # as_view() on it
    callable_object = product_detail.as_view()

    # the request is then passed as an argument to the callable object or view 
    # to form the response object
    response = callable_object(request, slug=product.slug)
    
    assertContains(response, product.name)

# Test for models string representation 
def test__str__():
    # creating an instance of a Category
    category = CategoryFactory()

    # creating an instance of a Shop_Category
    shop_category = ShopCategoryFactory()

    # creating an instance of a Shop
    shop = ShopFactory(category=shop_category)

    # creating an instance of a Product
    product = ProductFactory(category=category, shop=shop)

    # creating an instance of DeliveryPerson
    delivery_person = DeliveryPersonFactory()

    # string representaion of a delivery person object 
    assert delivery_person.__str__() == delivery_person.name
    assert str(delivery_person) == delivery_person.name

    # string representation of a shop category object
    assert shop_category.__str__() == shop_category.name 
    assert str(shop_category) == shop_category.name

    # string representaion of a category object
    assert category.__str__() == category.name_of_category
    assert str(category) == category.name_of_category

    # string representaion of a shop
    assert shop.__str__() == shop.name
    assert str(shop) == shop.name

    # string representation of product object
    assert product.__str__() == product.name
    assert str(product) == product.name

