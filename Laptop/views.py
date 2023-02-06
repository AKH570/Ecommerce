from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def laptop_master(request):
    return HttpResponse ("Welcome to my Laptop Zone")