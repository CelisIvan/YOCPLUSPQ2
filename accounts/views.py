from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate

from .forms import RegisterForm

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.age = form.cleaned_data.get('age')
            user.profile.estado = form.cleaned_data.get('estado')
            user.profile.empresa = form.cleaned_data.get('empresa')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect("/")    
    else:
        form = RegisterForm()
    return render(request,'signup.html',{"form":form})
