from django.conf.urls import url
from . import views


app_name = 'ambient_data'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail')
]
