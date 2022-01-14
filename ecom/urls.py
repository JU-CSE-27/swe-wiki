
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('app_login.urls')),
    path('showbkash/',views.bkashs, name= "bkash"),
    path('',views.index, name= "index"),
    path('product/',views.products, name= "products"),
    path('sketch/', include('sketch.urls')),
    path('added/', include('app_AddProduct.urls')),
    path('bkash/', include('app_BkashPayment.urls')),
    path('paytm/', include('payments.urls')),
    path('makepayment/', include('app_MakePayment.urls')),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
