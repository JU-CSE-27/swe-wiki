
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='app_viewProduct'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include(('app_login.urls'),namespace='userLog')),
    path('shopping_cart/',include('shopping_cart.urls')),
    path('products/',include(('app_viewProduct.urls'),namespace='viewProduct')),


    path('',views.index, name= "index"),
]

if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)