from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


@login_required
def index(response):
        return render(context={}, request=response, template_name="dashboard/index.html")