from django import forms
from django.core import validators

class UserInfo(forms.Form):
    first_name = forms.CharField(label='',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name =forms.CharField(label='',required=False,widget=forms.TextInput(attrs={'class':'form-control zmdi zmdi-account material-icons-name','placeholder':'Last name'}))
    email = forms.EmailField(label='',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),validators=[validators.MaxLengthValidator(10)])
    usercode = forms.IntegerField(label='',min_value=1,widget=forms.TextInput(attrs={'placeholder':'User code'}),help_text='You must fill up this field') 
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),min_length=8,max_length=12)
    repassword = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-password'}),min_length=8,max_length=12)
    textbox = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),error_messages={'required':'Please write some here'})
    checkbox =forms.BooleanField(label='',error_messages={'required':'Agreed with this'},help_text='Agreed')
