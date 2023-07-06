from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.forms.models import ModelForm
from django.utils.translation import gettext, gettext_lazy as _
from .models import BlogPost



class SingupForm(UserCreationForm):
    password1 = forms.CharField(label='Create Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Conform Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':True}))
    password = forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs=
    {'autocomplete':'current_password','class':'form-control'}))        


class AddPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__' 
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'descrip':forms.Textarea(attrs={'class':'form-control'}),
        }
