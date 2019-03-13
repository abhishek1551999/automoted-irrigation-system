from django.conf.urls import include,url
from . import views
urlpatterns = [
    url(r'^$', views.index ,name = "index") ,
    url(r'^get/$', views.getdata ,name ="get"),
    url(r'^general/$', views.general ,name='general'),
    url(r'^gen1/$', views.gen1 ,name='gen1'),
    url(r'^create/',views.create,name = 'create'),
]
