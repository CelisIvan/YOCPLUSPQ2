from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField()
    estado = forms.ModelChoiceField(
        label=u'Estado',
        queryset=Estado.objects.all()
    )
    empresa = forms.CharField()
    
    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","password1","password2", "age","estado","empresa"]

