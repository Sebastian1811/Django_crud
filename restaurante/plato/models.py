
from django.db import models


# Create your models here.
class Plato(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    tiempo_preparaciona = models.IntegerField(default=30)
    categoria = models.CharField(max_length=30,default="comida")
    ingredientes = models.ForeignKey('Alimento',on_delete=models.CASCADE,default=0)

class Alimento(models.Model):
    id = models.IntegerField(primary_key=1)
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
