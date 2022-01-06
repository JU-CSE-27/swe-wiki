from django.urls import path
from app_image import views


app_name='app_image'

urlpatterns = [
    path('',views.index ),

    ]
