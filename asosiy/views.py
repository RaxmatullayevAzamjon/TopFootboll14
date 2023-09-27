from django.shortcuts import render
from .models import *
def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,'about.html')

def players20(request):
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




