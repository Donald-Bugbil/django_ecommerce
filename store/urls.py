from django.urls import path
from . import views 

app_name = 'store'

urlpatterns = [

    path(
        route='store/',
        view=views.Store.as_view(),
        name='store'
        ),
    path(
        route='<slug:slug>/',
        view=views.detail_store.as_view(),
        name='detail_store'
    ),
    path(
        route='product/<slug:slug>/',
        view=views.product_detail.as_view(),
        name='productdetail'
        )
]