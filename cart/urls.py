from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path(
        route='add/<int:product_id>/',
        view= views.Add_to_cart.as_view(),
        name = 'cart_add'
    ),
    path(
        route='remove/<int:product_id>/',
        view=views.Remove.as_view(),
        name='cart_remove'
    ),
    path(
        route='',
        view=views.Cart_detail.as_view(),
        name='cart_detail'
    )
]