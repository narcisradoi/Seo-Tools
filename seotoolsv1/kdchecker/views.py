from django.shortcuts import render
from django.http import HttpResponse
from . import keyworddensity

# Create your views here.

import datetime

def index(request):
    return HttpResponse("Keyword percentage is: " + keyworddensity.perc + "%")
