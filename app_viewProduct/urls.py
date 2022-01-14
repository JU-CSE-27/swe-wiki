from django.urls import path
from app_viewProduct import views


app_name='app_image'

urlpatterns = [
    path('',views.product_page, name='viewProduct' ),
    path('latest/',views.latestProduct_page,name='latest'),
    path('high/',views.toHighProduct_page,name='high'),
    path('low/',views.toLowProduct_page,name='low'),
    path('search/',views.searchProduct_page,name='search'),

    ]

