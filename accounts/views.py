from django.shortcuts import render, redirect
from .models import *
from .models import add_user_to_list_of_attendees
from django.views.generic import ListView, DetailView
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

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
            boletos=Boleto.objects.all()
            return render(request,"accounts/eventos.html",{'eventos':eventos , 'boletos':boletos})
        else:
             return redirect("/") 
        
class EventListView(ListView):
    model = Evento
    template_name = 'accounts/eventos.html'
    context_object_name = 'eventos'

def event_add_attendance(request, pk):
    this_event = Evento.objects.get(pk=pk)
    user_id=request.user
    
    flag = Boleto.objects.filter(evento=this_event,user=user_id).exists()
    if not Boleto.objects.filter(evento=this_event,user=user_id).exists():
        add_user_to_list_of_attendees(self=this_event, user=request.user)
        boleto = Boleto.objects.filter(evento=this_event,user=user_id)
        
        return render(request,"inscription.html",{'this_event':this_event,'flag':flag,'boleto':boleto})
    else:
        return render(request,"inscription.html",{'this_event':this_event,'flag':flag})

class EventDetailView(DetailView):
    model = Evento
    



def register_event(request):
    if request.method == "GET":
        return render(request,"register_event.html")
