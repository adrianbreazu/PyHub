from django import forms


class AmbientData(forms.Form):
    sensor_id = forms.UUIDField()
    temperature = forms.FloatField()
    humidity = forms.FloatField()
    pressure = forms.FloatField()
