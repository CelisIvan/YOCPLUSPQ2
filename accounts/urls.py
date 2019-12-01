from django.urls import path,include
from django.conf.urls import url

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('eventos',views.getEventos)
router.register('estados',views.getEstados)



urlpatterns = [
    path('', views.home, name='accounts-name'),
    path('register/', views.register, name='accounts-register'),

    path('eventos/',views.eventos),

    path('register_event/',views.register_event),


    path('api/',include(router.urls)),



]
