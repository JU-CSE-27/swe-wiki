
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog1.urls')),
    path('froala_editor/', include('froala_editor.urls'))
]
