from django.urls import path
from django.urls import path
from app_login import views



app_name='app_login'



urlpatterns = [
    path('home/', views.home_page, name="home"),
	path('register/', views.registration_Page, name="register"),
    path('login/', views.login_page, name="login"),  
	path('logout/', views.logout_page, name="logout"),
	path('profile/', views.userProfile_page, name="profile"),
	path('profile/edit/',views.editProfile_page, name="editProfile" ),
	path('change-password/',views.changePassword_page, name="changePassword" ),
]