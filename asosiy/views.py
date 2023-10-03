from django.shortcuts import render
from .models import *
def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,'about.html')

def players20(request):
    content = {
        "players20": Player.objects.filter()
    }
    return render(request,"U-20 players.html")

def england(request):
    return render(request, "england.html")

def country_clubc(request):
    return render(request, "country-clubc.html")

def players(request):
    content = {
        "players":Player.objects.all()
    }
    return render(request, "players.html",content)

def clubs(request):
    content = {
        "clubs": Club.objects.all()
    }
    return render(request,"clubs.html",content)

def tryouts(request):
    return render(request,"tryouts.html")


def latest_transfers(request):
    hozirgi = Hozirgi_mavsum.objects.last().h_mavsum
    transferlar = Transfer.objects.filter(mavsum=hozirgi)
    content = {
        "transfers": transferlar
    }
    return render(request,"latest-transfers.html",content)

def stats(request):
    return render(request,"stats.html")

def transfer_record(request):
    content = {
        "transfers": Transfer.objects.filter(narx__gt=50)
    }
    return render(request,"transfer-records.html",content)

def davlat_clublari(requsets, nom):
    content = {
        "clublar": Club.objects.filter(davlat=nom.capitalize())
    }
    return render(requsets, "england.html",content)

def season(request,mavsum):
    content = {
        "transferlar": Transfer.objects.filter(mavsum=mavsum)
    }
    return render(request,"2017-18season.html",content)
