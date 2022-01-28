
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('app_login.urls')),
    path('comment/',include('app_comment.urls')),
    path('',views.index, name= "index"),
    path('products/',include(('app_viewProduct.urls'),namespace='viewProduct')),
    path('product/',include('app_products.urls')),
]

if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
