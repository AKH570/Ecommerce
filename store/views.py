from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from.forms import UserInfo

# Create your views here.
def all_products(request):
    return render(request,'store/allproduct.html')

def store_det(request):
    product_detail = Product.objects.all()
    return render(request,'store/product.html',{'prod_det':product_detail})

def signup(request):
    form = UserInfo(auto_id=True,label_suffix='')
    context = {'frm':form}
    return render(request,'store/signup.html',context)
