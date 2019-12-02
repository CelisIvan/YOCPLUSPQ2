from django.urls import path
from .views import EventListView , EventDetailView
from . import views


urlpatterns = [
    path('', views.home, name='accounts-name'),
    path('register/', views.register, name='accounts-register'),

    path('eventos/',views.eventos),
    path('evento/<int:pk>/',EventDetailView.as_view(),name='evento-detail'),
    path('eventoadd/<int:pk>/',views.event_add_attendance,name='evento-inscribirse'),
    path('register_event/',views.register_event),

]
