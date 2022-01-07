from django.urls import path
from shopping_cart import views





app_name='shopping_cart'




urlpatterns = [
    path('',views.cart,name='cart'),
    path('',views.head,name='head'),

	
]

