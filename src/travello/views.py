from django.shortcuts import render
from .models import Destination

def index(request):
    dests = Destination.objects.all()
        
    return render(request, "index.html", {'dests': dests})

def lista_destinos(request):
    destinos = Destination.objects.all()
    return render(request, "lista_destinos.html", {'destinos': destinos})

def editar_destino(request):
    pass

def eliminar_destino(requets):
    pass

def crear_destino(requets):
    pass