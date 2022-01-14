
from django.contrib import admin
#from livechat.chat import admin
from django.urls import path,include
from ecom import views as ecom_views
from livechat.chat import views as livechat_views
from events.events import views as event_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('app_login.urls')),
    path('',ecom_views.index, name= "index"),
    path('contact/',ecom_views.contact, name= "contact"),
    path('product/',ecom_views.contact, name= "product"),
    path('blog/',ecom_views.contact, name= "blog"),
    path('about/',ecom_views.contact, name= "about"),
    
    path('home/',livechat_views.home, name= "home"),
    path('room/',livechat_views.room, name= "room"),
    path('event/',event_views.event_home, name= "event_view"),
    path('myevent/',event_views.add_event, name= "event_view"),
    #path('event',include('events.events.urls')),
]
