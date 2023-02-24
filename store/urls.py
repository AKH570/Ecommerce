from django.urls import path
from store import views

urlpatterns = [
    			path('pd/', views.store_det,name='product'), 
                path('', views.all_products,name='all'), 
]