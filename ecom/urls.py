
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('app_login.urls')),
    path('',views.index, name= "index"),
    path('contact.html',views.contact, name= "contact"),
    path('product.html',views.contact, name= "product"),
    path('blog.html',views.contact, name= "blog"),
    path('about.html',views.contact, name= "about"),
]
