from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(BoardType)
admin.site.register(CommunicationType)
admin.site.register(SensorType)
admin.site.register(ReadDataRecurrency)
admin.site.register(Sensor)
admin.site.register(ReadData)