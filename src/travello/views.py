from django.shortcuts import render, redirect
from .models import Destination

def index(request):
    dests = Destination.objects.all()
        
    return render(request, "index.html", {'dests': dests})

def lista_destinos(request):
    destinos = Destination.objects.all()
    return render(request, "lista_destinos.html", {'destinos': destinos})

def crear_destino(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        price = request.POST['price']
        offer = 'offer' in request.POST
        img = request.FILES.get('img')

        destino = Destination(
            name=name,
            desc=desc,
            price=price,
            offer=offer,
            img=img
        )

        destino.save()
        return redirect("lista_destinos")
    
    else:
        return render(request, 'crear_destino.html')

def editar_destino(request):
    pass

def eliminar_destino(requets):
    pass
