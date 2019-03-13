from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^temperature/', include('temperature.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('temperature.urls'))
]

