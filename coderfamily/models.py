from django.db import models

# Create your models here.

class Familia(models.Model):

    nombre = models.CharField(max_length=30)

class Padre(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Madre(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Tio(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Primo(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()