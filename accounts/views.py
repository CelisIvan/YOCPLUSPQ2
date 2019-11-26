from django.shortcuts import render, redirect
from .models import *

from .forms import RegisterForm

def home(request):
    return render(request,'registration/login.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")    
    else:
        form = RegisterForm()
    return render(request,'signup.html',{"form":form})
