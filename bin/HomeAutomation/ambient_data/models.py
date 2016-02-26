from django.db import models
import datetime


class BoardType(models.Model):
    type = models.CharField(max_length= 50)

    def __str__(self):
        return self.type


class CommunicationType(models.Model):
    type = models.CharField(max_length= 70)

    def __str__(self):
        return self.type


class SensorType(models.Model):
    type = models.CharField(max_length= 70)

    def __str__(self):
        return self.type


class ReadDataInterval(models.Model):
    interval = models.CharField(max_length=70)

    def __str__(self):
        return self.interval


class Sensor (models.Model):
    unique_number = models.UUIDField()
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    board_type = models.ForeignKey(BoardType)
    communication_type = models.ForeignKey(CommunicationType)
    sensor_type = models.ForeignKey(SensorType)
    read_data_interval = models.ForeignKey(ReadDataInterval)

    def __str__(self):
        return self.name


class ReadData(models.Model):
    type = models.CharField(max_length=70)
    value = models.CharField(max_length=300)
    sensor = models.ForeignKey(Sensor)
    read_datetime = models.DateTimeField()

    def __str__(self):
        return ':'.join([self.sensor.name,self.type,str(self.read_datetime)])


def add_ambient_data(sensor_id, temperature, humidity, pressure):
    read_data = datetime.datetime.now()
    sensor = Sensor.objects.get(unique_number=sensor_id)
    print('!!! model sensor =' + str(sensor))
    ReadData.objects.create(
            type='temperature',
            value=temperature,
            sensor=sensor,
            read_datetime=read_data
    )
    ReadData.objects.create(
            type='humidity',
            value=humidity,
            sensor=sensor,
            read_datetime=read_data
    )
    ReadData.objects.create(
            type='pressure',
            value=pressure,
            sensor=sensor,
            read_datetime=read_data
    )
