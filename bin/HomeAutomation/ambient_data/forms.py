from django import forms


class AmbientData(forms.Form):
    print('begin ambient_data form')
    sensor_id = forms.UUIDField()
    temperature = forms.FloatField()
    humidity = forms.FloatField()
    print('end ambient_data form')
