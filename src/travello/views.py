from django.shortcuts import render, redirect
from .models import Destination

def index(request):
    dests = Destination.objects.all()
        
    return render(request, "index.html", {'dests': dests})

def lista_destinos(request):
    destinos = Destination.objects.all().order_by('name')
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

def editar_destino(request, id):
    destino = Destination.objects.get(id=id)

    if request.method == 'POST':
        destino.name = request.POST['name']
        destino.desc = request.POST['desc']
        destino.price = request.POST['price']
        destino.offer = 'offer' in request.POST
        if 'img' in request.FILES:
            if destino.img:
                destino.img.delete(save=False)
            destino.img = request.FILES.get('img')

        destino.save()
        return redirect("lista_destinos")
    
    else:
        return render(request, 'editar_destino.html', {'destino': destino})

def eliminar_destino(request, id):
    destino = Destination.objects.get(id=id)

    if request.method == 'POST':
        if destino.img:
            destino.img.delete(save=False)

        destino.delete()
        return redirect('lista_destinos')

    else:
        return render(request, 'eliminar_destino.html', {'destino': destino})
        

