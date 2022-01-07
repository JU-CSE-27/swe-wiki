from django.urls import path
from app_image import views


app_name='app_image'

urlpatterns = [
    path('',views.product_page ),
    path('latest/',views.toLowProduct_page),
    path('high/',views.toHighProduct_page),
    path('latest/',views.toLowProduct_page),

    ]

