from django.shortcuts import render
from django.http import HttpResponse
from . import keyworddensity

# Create your views here.

def index(request):
    return render(request, 'kdchecker/index.html')

def process(request):
    if request.method == 'POST':
        text = request.POST['txtField']
        print(text)
    return HttpResponse(text)