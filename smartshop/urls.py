from django.urls import path
from smartshop import views

urlpatterns = [
    			path('', views.home,name='home'), 
]