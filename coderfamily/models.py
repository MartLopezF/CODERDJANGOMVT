from django.db import models

# Create your models here.

class Familia(models.Model):

    nombre = models.CharField(max_length=30)
    relacion = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_de_ingreso = models.DateTimeField()