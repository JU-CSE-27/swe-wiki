from django.urls import path
from django.urls.resolvers import URLPattern
from app_product import views

app_name="app_product"

urlpatterns=[
    # path('',views.product_page, name= "products"),
    # path('',views.image_page, name= "image"),

    path('image/', views.image_page, name="image"),
    path('product/', views.product_page, name="product"),
    
]