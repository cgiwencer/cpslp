from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class usuario(models.Model):
    codigo=models.CharField(primary_key=6, max_length=6)
    nombre=models.CharField(max_length=150)
    nomusu=models.CharField(max_length=50)
    clave=models.CharField(max_length=10)
    
    
    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.nombre, self.nomusu)
