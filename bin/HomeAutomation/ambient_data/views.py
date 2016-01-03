from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Sensor


def index(request):
    sensors_list = Sensor.objects.order_by('name')
    context = {'sensors_list': sensors_list}
    return render(context=context, request=request, template_name='ambient_data/index.html')


def detail(request, id):
    sensor = get_object_or_404(Sensor, id=id)
    readdata_list = sensor.readdata_set.all()
    return render(request=request, template_name='ambient_data/detail.html', context={
        'sensor': sensor, 'readdata_list': readdata_list
    })
