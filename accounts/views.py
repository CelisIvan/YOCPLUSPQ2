from django.shortcuts import render, redirect
from .models import *

from .forms import RegisterForm
from django.contrib.auth import login, authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, viewsets

from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.generics import ListCreateAPIView

from .serializers import *

import json

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


def eventos(request):
    if request.method  == "GET":
        if User.is_authenticated:
            eventos=Evento.objects.all()
            return render(request,"eventos.html",{'eventos':eventos})
        else:
             return redirect("/")



def register_event(request):
    if request.method == "GET":
        return render(request,"register_event.html")


def empty_view(self):
    content = {'Por favor, intente nuevamente': 'No se ha encontrado nada el recurso solicitado.'}
    return Response(content, status=status.HTTP_404_NOT_FOUND)

#@api_view(["GET"])
class getEventos(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,IsAdminUser,)
    queryset=Evento.objects.all()
    serializer_class=EventSerializer


class getEstados (viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,IsAdminUser,)
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
