from django.urls import path
from shopping_cart import views





app_name='shopping_cart'




urlpatterns = [
    path('',views.cart_page,name='cart_page'),
    path('',views.headImg_page,name='headImg_page'),

	
]

