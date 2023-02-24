from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . forms import UserCustForm

# Create your views here.

def userform(request):
    if request.method == 'POST':
        uform = UserCustForm(request.POST) # in replaced of UserCreationForm we call UserCustForm from forms.py
        if uform.is_valid():
            uform.save()
    else:
        uform = UserCustForm() # in replaced of UserCreationForm we call UserCustForm from forms.py
    return render(request,'profile/registration.html',{'form':uform})