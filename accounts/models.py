from django.db import models

# Create your models here.
class Person(models.Model):
    edad = models.IntegerField()
    empresa = models.CharField(max_length=50)


class Boleto(models.Model):
    codigo = models.CharField(max_length=50)



class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    costo = models.FloatField()

    empresa = models.CharField(max_length=50)
