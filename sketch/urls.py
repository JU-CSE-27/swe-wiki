from django.urls import path
from sketch import views

app_name="sketch"

urlpatterns=[
    path('', views.sketch_page, name="home"),   
]