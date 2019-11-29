from django.shortcuts import render, redirect
from .models import *

from .forms import RegisterForm

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(request,'signup.html',{"form":form})


def eventos(request):
    if request.method  == "GET":
        return render(request,"eventos.html")

def register_event(request):
    if request.method == "GET":
        return render(request,"register_event.html")
