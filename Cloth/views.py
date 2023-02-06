from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def cloth_master(request):
    color='red'
    brand ='Bangladeshi'
    size = 'XXL'
    cloths_details ={'cl':color,'br':brand,'sz':size}
    return render(request,'Cloth/cloth.html',cloths_details)