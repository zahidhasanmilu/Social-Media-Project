from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile

from App_Login.models import UserProfile

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':'Enter your email here'}))
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':'Enter username Here'}))
    password1 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')
        
        
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':'Enter username here'}))
    password = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        model = User
        fields = ('username','password')
        
class EditProfile(forms.ModelForm):
    class Meta:
        model =UserProfile
        fields ='__all__'