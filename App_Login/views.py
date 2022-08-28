from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .forms import CreateUserForm,UserLoginForm
from .models import UserProfile


# Create your views here.
def signup(request):
    form = CreateUserForm()
    registered = False    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            registered =True
            user = UserProfile(user=user)
            return 
    return render(request, 'account/signup.html', context={'form':form, 'registered':registered})


def signin(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.changed_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
    return render(request, 'account/login.html', context={'form':form,})
