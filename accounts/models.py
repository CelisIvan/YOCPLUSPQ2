from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Estado(models.Model):
    nombre = models.CharField(max_length = 50)
    def __str__(self):
        return self.nombre

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True,null=True)
    empresa = models.CharField(max_length=50, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    costo = models.FloatField()
    descripcion = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    siglas = models.CharField(max_length=50)
    fecha = models.DateField()
    asistentes = models.IntegerField()
    def __str__(self):
        return self.nombre

class Boleto(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=50)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)



