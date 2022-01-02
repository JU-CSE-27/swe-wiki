from django.urls import path
from django.urls import path
from app_login import views



app_name='app_login'



urlpatterns = [
    path('home/', views.home, name="home"),
	path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
]