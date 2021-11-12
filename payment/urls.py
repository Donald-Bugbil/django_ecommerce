from django.urls import path 
from . import views 

app_name = 'payment'

urlpatterns = [
    path(
        route= 'process/<int:order_id>/',
        view= views.PaymentProcess.as_view(),
        name = 'paymentprocess'
    )
]