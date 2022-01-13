

from django.urls import path
from .import views
urlpatterns=[
# <<<<<<< HEAD
    path('', views.addproduct_page,name='addproduct'),   
# =======
# <<<<<<< HEAD
    path('', views.addproduct_page,name='addproduct'),   
# =======
    path('', views.addproduct_page),   
# >>>>>>> faf07d4f49f8f244dc3f00cf53f2fca34ec0286b
# >>>>>>> bed44d0afa3ec01cd171905be06cae7f5c253dd6
]