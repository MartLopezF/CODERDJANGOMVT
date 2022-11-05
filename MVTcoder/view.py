from django.http import HttpResponse
from django.db import models
from django.template import Context, loader, Template
from django.shortcuts import render



def familiares(request):

    lista_familiares = ["Joaquin Lopez", "Marsiol Fernandez" , "Juan Hernandez", "Ignacio Hernandez"]
    datos = {"relacion": "familiares", "lista_de_familia": lista_familiares}

    plantilla = loader.get_template("templates.html")
    documento = plantilla.render(datos)
    #contexto = Context()
    
    HttpResponse(documento)

    pass


def Padre(request):

    return render(request, "templates_padre.html")

def Madre(request):

    return render(request, "templates_madre.html")

def Tio(request):

    return render(request, "templates_tio.html")

def Primo(request):

    return render(request, "templates_primo.html") 

