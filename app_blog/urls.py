from django.urls import path
from .views import *

urlpatterns = [
    path('' , blog_page, name="blog"),
    path('blog-detail/<m_slug>' , blog_detail_page , name="blog_detail"),
    path('add-blog/' , add_blog_page, name="add_blog"),

]
