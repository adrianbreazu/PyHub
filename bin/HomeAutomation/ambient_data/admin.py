from django.contrib import admin

from .models import *
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = ReadData
    extra = 2


class SensorAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(BoardType)
admin.site.register(CommunicationType)
admin.site.register(SensorType)
admin.site.register(ReadDataRecurrency)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(ReadData)