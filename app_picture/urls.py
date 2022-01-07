from django.urls import path
from django.urls.resolvers import URLPattern
from app_picture import views

app_name="app_picture"

urlpatterns=[
    path('pictures/', views.picture_page, name="pictures"),   
]