from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mobile_master(request):
    return HttpResponse ("Welcome to my Mobile Zone")