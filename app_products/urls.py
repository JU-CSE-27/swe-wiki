from django.urls import path
from app_products import views



app_name='app_products'



urlpatterns = [
    path('', views.product_page, name="product"),

]