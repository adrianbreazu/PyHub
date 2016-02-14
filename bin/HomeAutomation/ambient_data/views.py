from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from django.core import serializers
from .forms import AmbientData


@login_required
def index(request):
    sensors_list = Sensor.objects.order_by('name')
    context = {'sensors_list': sensors_list}
    return render(context=context,
                  request=request,
                  template_name='ambient_data/index.html'
                  )


@login_required
def maintain(request):
    sensors_list = Sensor.objects.order_by('name')
    read_data_interval = ReadDataInterval.objects.order_by('interval')
    board_type = BoardType.objects.order_by('type')
    communication_type = CommunicationType.objects.order_by('type')
    sensor_type = SensorType.objects.order_by('type')
    context = {'sensors_list': sensors_list,
               'board_type': board_type,
               'read_data_interval': read_data_interval,
               'communication_type': communication_type,
               'sensor_type': sensor_type,
               }
    return render(context=context,
                  request=request,
                  template_name='ambient_data/maintain.html'
                  )


@login_required
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


@csrf_exempt
def sensor_temperature_and_humidity(request):
    print('begin sensor_temperature_and_humidity view')
    if request.method == "POST":
        print('Raw data : %s' % request.body)
        retrieve_json_data = json.loads(request.body.decode('utf-8'))
        add_ambient_data(sensor_id=retrieve_json_data['sensor_id'],
                         temperature=retrieve_json_data['temperature'],
                         humidity=retrieve_json_data['humidity'])
        return HttpResponse("Bravo Bruno")
        #form = AmbientData(request.POST)
        #if form.is_valid():
        #    add_ambient_data(sensor_id=form.cleaned_data['sensor_id'],
        #                     temperature=form.cleaned_data['temperature'],
        #                      humidity=form.cleaned_data['humidity'])
        #    return HttpResponse("Bravo Bruno")
        #else:
        #    return HttpResponse("Nu Bruno !")
    else:
        return HttpResponse("Nu Bruno !!")
