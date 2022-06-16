from django.db import models
from django.forms import DateField

# Create your models here.
# se crea una clase por cada tabla que necesite en la db

class Integrantes(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    fechaNacimiento=DateField()
    itsAlive=models.BooleanField()