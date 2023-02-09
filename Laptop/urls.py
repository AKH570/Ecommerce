from django.urls import path
from Laptop import views

urlpatterns = [
    			path('', views.laptop_master,name='laptop'), 
]