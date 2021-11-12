import pytest 
from django.test import RequestFactory as rf
pytestmark = pytest.mark.django_db
from pytest_django.asserts import assertContains
from django.urls import reverse 


from .views import HomePage

# Create your tests here.

def test_homepage_view(rf):
    #url for homepage
    url  = reverse('pages:home')
    
    # getting the request object
    request = rf.get(url)

    # views are functions but you can write them in classes and calling  
    # as_view() on it
    callable_object = HomePage.as_view()

    # the request is then passed as an argument to the callable object or view 
    # to form the response object
    response = callable_object(request)

    assertContains(response, status_code=200, text='Shops')
