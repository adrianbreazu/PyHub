import os
import django
import sys
import RPi.GPIO as GPIO
import dht11
import time
import datetime


# setup django context
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HomeAutomation.settings")
django.setup()


# load django models
from ambient_data.models import *
from django.utils import timezone

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


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
instance = dht11.DHT11(pin = 4)

while True:
    result = instance.read()
    if result.is_valid():
        #print("Last valid input: " + str(datetime.datetime.now()))
        #print("Temperature: %d C" % result.temperature)
        #print("Humidity: %d %%" % result.humidity)
        ambient_data(12345678901234567890123456789012, result.temperature, result.humidity)
    time.sleep(3600)