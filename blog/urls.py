from django.urls import path
from django.urls import path
from blog import views



app_name='blog'



urlpatterns = [
    path('blog/', views.blog, name="blog"),
	
    
]