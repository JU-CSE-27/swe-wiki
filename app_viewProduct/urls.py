from django.urls import path
from app_viewProduct import views


app_name='app_image'

urlpatterns = [
    path('',views.product_page, name='viewProduct' ),
    path('latest/',views.latestProduct_page,name='latest'),
    path('high/',views.toHighProduct_page,name='high'),
    path('low/',views.toLowProduct_page,name='low'),
    path('regOffer/',views.regularOffer_page, name='regOffer' ),
    path('stuOffer/',views.stuOffer_page, name='stuOffer' ),
    path('eidOffer/',views.eidOffer_page, name='eidOffer' ),

    ]

