
from django.shortcuts import render
from .models import *

def home(request):
    return render(request,'registration/login.html')

def register(request):
    return render(request,'signup.html')
