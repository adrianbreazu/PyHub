from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    return render(context={}, request=response, template_name="sprinkler_control/index.html")