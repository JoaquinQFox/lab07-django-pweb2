from django.shortcuts import render
from .models import Destination

def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.price = 700
    dest1.img = 'destination_1.jpg'

    dest2 = Destination()
    dest2.name = 'Mexico'
    dest2.desc = 'Tierra Amarilla'
    dest2.price = 500
    dest2.img = 'destination_2.jpg'
    
    dest3 = Destination()
    dest3.name = 'Peru'
    dest3.desc = 'Rica Cultura'
    dest3.price = 800
    dest3.img = 'destination_3.jpg'

    dests = [dest1, dest2, dest3]
    
    return render(request, "index.html", {'dests': dests})