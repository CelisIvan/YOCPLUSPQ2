from django.db import models


# Create your models here.

class Estado(models.Model):
    nombre = models.CharField(max_length = 50)
    
class Person(models.Model):
    edad = models.IntegerField()
    empresa = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)



class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    costo = models.FloatField()
    descripcion = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    siglas = models.CharField(max_length=50)
    fecha = models.DateField()
    asistentes = models.IntegerField()

class Boleto(models.Model):
    codigo = models.CharField(max_length=50)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)


