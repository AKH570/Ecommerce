from django import forms

class UserInfo(forms.Form):
    first_name = forms.CharField(label='First Name',required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name =forms.CharField(label='Last Name',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    