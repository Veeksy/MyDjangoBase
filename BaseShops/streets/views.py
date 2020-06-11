from django.http import HttpResponse
from django.shortcuts import render
from streets.models import *
from city.models import *


def ViewStreets(request) -> render:
    street = Streets.objects.all()
    return render(request, 'MainApp/streets.html', {"street": street})


