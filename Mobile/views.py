from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mobile_master(request):
    return render (request,"mobile/mobile.html")