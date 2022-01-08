from django.urls import path
from app_comment import views



app_name='app_comment'


urlpatterns = [
    path('', views.comment_page, name = "comment"),
   

]