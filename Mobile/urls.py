from django.urls import path
from Mobile import views

urlpatterns = [
    			path('', views.mobile_master,name='mobile'), 
]