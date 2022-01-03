from django.urls import path
from django.urls.resolvers import URLPattern
from app_product import views

app_name="app_product"

urlpatterns=[
    path('',views.product_page, name= "products"),
]