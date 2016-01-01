from django.db import models


class BoardType(models.Model):
    type = models.CharField(max_length= 50)


class CommunicationType(models.Model):
    type = models.CharField(max_length= 70)


class SensorType(models.Model):
    type = models.CharField(max_length= 70)


class ReadDataRecurrency(models.Model):
    recurrency = models.CharField(max_length=70)


class Sensor (models.Model):
    unique_number = models.UUIDField()
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    board_type = models.ForeignKey(BoardType)
    communication_type = models.ForeignKey(CommunicationType)
    sensor_type = models.ForeignKey(SensorType)
    read_data_recurrency = models.ForeignKey(ReadDataRecurrency)
    read_datetime = models.DateTimeField(auto_now=True, name="read value date time")


class ReadData(models.Model):
    type = models.CharField(max_length=70, name='read data type')
    value = models.CharField(default=0, name = 'read data value')
    sensor = models.ForeignKey(Sensor)