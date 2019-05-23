from django.db import models

# Create your models here.
class Auto(models.Model):
    Modelo = models.CharField(max_length = 200, null= False)
    Marca =  models.CharField(max_length = 200, null= False)
    Transmision =  models.CharField(max_length = 200, null= False)
    Tipo =  models.CharField(max_length = 200, null= False)
    Puertas =  models.FloatField()