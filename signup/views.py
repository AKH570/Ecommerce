from django.shortcuts import render
from.forms import UserInfo
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserInfo(request.POST)
        print(form)
        print('Execute post')
        print(form.cleaned_data)
        print('1st name:',form.cleaned_data['first_name'])
        print('2nd name:',form.cleaned_data['last_name'])

    else:
        form = UserInfo(auto_id=True,label_suffix='')
        print('Execute GET')
    return render(request,'profile/signup.html',{'frm':form})