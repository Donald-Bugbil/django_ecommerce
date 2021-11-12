from django.urls import path 
from . import views 
app_name = 'order'

urlpatterns = [
    path(
        route="create/<int:product_id>/",
        view = views.OrderCreate.as_view(),
        name = "ordercreate"
    )

]