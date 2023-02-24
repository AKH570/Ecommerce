from django.urls import path
from registration import views


urlpatterns = [
                path('', views.userform,name='regi'), 
]