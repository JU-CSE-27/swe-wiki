from django.urls import path
from django.urls import path
from app_login import views



app_name='app_login'



urlpatterns = [
    path('home/', views.home_page, name="home"),
	path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
	path('logout/', views.logout_page, name="logout"),
]
