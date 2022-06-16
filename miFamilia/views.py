from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from miFamilia.models import Integrantes

def inicio(request):
    return render(request,"miFamilia/inicio.html")

def integrantes(request):

    familia= Integrantes.objects.all()
    return render(request,"miFamilia/integrantes.html", {"familia":familia})

