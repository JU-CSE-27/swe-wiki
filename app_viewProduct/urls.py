from django.urls import path
from app_viewProduct import views


<<<<<<< HEAD
app_name='app_viewProduct'

urlpatterns = [
    path('home/', views.home_page, name="home"),
=======
app_name='app_image'

urlpatterns = [
>>>>>>> 81a0ce53034d1a5f5003e5222084c40ad0d2f602
    path('',views.product_page, name='viewProduct' ),
    path('latest/',views.latestProduct_page,name='latest'),
    path('high/',views.toHighProduct_page,name='high'),
    path('low/',views.toLowProduct_page,name='low'),

    ]

