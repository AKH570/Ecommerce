from django.urls import path
from . import views

urlpatterns = [
    			path('', views.cloth_master,name='cloth'), 
]