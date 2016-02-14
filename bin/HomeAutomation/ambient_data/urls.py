from django.conf.urls import url
from . import views


app_name = 'ambient_data'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^maintain/$', views.maintain, name='maintain'),
    url(r'^sensor_data$', views.sensor_temperature_and_humidity, name='sensor_temperature_and_humidity')
]
