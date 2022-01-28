from django.urls import path
from app_MakePayment import views

app_name="app_MakePayment"

urlpatterns=[
    path('', views.makepayment_page, name="home"), 
    # path('done/', views.new_page, name="home"),  
]