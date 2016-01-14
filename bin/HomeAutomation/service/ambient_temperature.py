import os
import django
import sys


# setup django context
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HomeAutomation.settings")
django.setup()


# load django models
from ambient_data.models import *
from django.utils import timezone


def ambient_data(sensor_id, temperature, humidity):
    sensor = Sensor.objects.get(unique_number=str(sensor_id))
    ReadData.objects.create(
            type='temperature',
            value=int(temperature),
            sensor=sensor,
            read_datetime=timezone.datetime.utcnow()
    )
    ReadData.objects.create(
            type='humidity',
            value=int(humidity),
            sensor=sensor,
            read_datetime=timezone.datetime.utcnow()
    )


# test by adding some data
ambient_data(12345678901234567890123456789012, 44, 88)