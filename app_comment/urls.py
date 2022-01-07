from django.urls import path
from app_comment import views



app_name='app_comment'



urlpatterns = [
    path('', views.comment_page, name="comment"),
    #path('liked/<pk>/', views.liked_page, name='liked_post'),
   # path('reply/<int:id>',views.reply_page,name="reply" ),

]
