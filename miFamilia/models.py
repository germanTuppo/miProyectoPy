from django.db import models
from django.forms import DateField

# Create your models here.
# se crea una clase por cada tabla que necesite en la db

class Integrantes(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    #tontillo, no había puesto models aca. Por eso no me creó el campo de la fecha. Maldición!
    fechaNacimiento=models.DateField()
    itsAlive=models.BooleanField()