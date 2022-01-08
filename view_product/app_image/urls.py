from django.urls import path
from app_image import views


app_name='app_image'

urlpatterns = [
    path('',views.product_page, name='viewProduct' ),
    path('latest/',views.latestProduct_page),
    path('high/',views.toHighProduct_page),
    path('low/',views.toLowProduct_page),

    ]

