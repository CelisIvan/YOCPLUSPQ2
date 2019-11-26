from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='accounts-name'),
    path('register/', views.register, name='accounts-register'),
    
]