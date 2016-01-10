from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Sensor
from django.core import serializers


def index(request):
    sensors_list = Sensor.objects.order_by('name')
    context = {'sensors_list': sensors_list}
    return render(context=context,
                  request=request,
                  template_name='ambient_data/index.html'
                  )


def detail(request, id):
    sensor = get_object_or_404(Sensor, id=id)
    data_list = sensor.readdata_set.all().order_by('read_datetime')
    temperature_list = sensor.readdata_set.filter(type='temperature').order_by('read_datetime')
    humidity_list = sensor.readdata_set.filter(type='humidity').order_by('read_datetime')

    return render(request=request,
                  template_name='ambient_data/detail.html',
                  context={'sensor': sensor,
                           'temperature_list': temperature_list,
                           'humidity_list': humidity_list,
                           'data_list': serializers.serialize('json', data_list)
                           })
