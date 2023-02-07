from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def laptop_master(request):
    return render (request,'laptop/laptop.html')