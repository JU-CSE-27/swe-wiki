
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('app_login.urls')),
    # path('',views.index, name= "index"),

    # path('',views.images, name= "images"),
    # path('image/',include('app_product.urls')),
    path('',views.products, name= "products"),
    path('product/',include('app_product.urls')),
    path('product/',views.products, name= "products"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
