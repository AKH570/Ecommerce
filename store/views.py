from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


# Create your views here.
def all_products(request):
    return render(request,'store/allproduct.html')

def store_det(request):
    product_detail = Product.objects.all()
    return render(request,'store/product.html',{'prod_det':product_detail})