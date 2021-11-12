from django.urls import path
from . import views

app_name = 'pages'

urlpatterns =[
    path(
    route='', 
    view= views.HomePage.as_view(), 
    name='home'),
]