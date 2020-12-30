from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def pyapi(request):
    return HttpResponse("Hello Pyapi")

def pyapihello(request):
    return HttpResponse("world")