from django.urls import path 
from .views import *

urlpatterns = [
    path('' , blog, name="blog"),
    path('blog-detail/<m_slug>' , blog_detail , name="blog_detail"),
    path('add-blog/' , add_blog, name="add_blog"),
   
]