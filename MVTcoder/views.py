from django.http import HttpResponse
from django.db import models
from django.template import Context, loader, Template
from django.shortcuts import render



def familiares(request):
    
    archivo = open(r"C:\Users\23mar\Desktop\CODER DJANGO MVT\MVTcoder\MVTcoder\plantillas\templates.html")
    plantilla = Template(archivo.read())
    archivo.close()


    datos = {"nombre": "Joaquin Lopez", "edad": 45 , "relacion": "Padre"}
    contexto = Context(datos)

    documento = plantilla.render(contexto)
    return HttpResponse(documento)

    
    #return render(request, "templates.html")
    


def Padre(request):

    return render(request, "templates_padre.html")

def Madre(request):

    return render(request, "templates_madre.html")

def Tio(request):

    return render(request, "templates_tio.html")


