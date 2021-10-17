from django.db import models
from .categoria import Categoria


class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.TextField(null=False)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fabricante =models.CharField(null=False,max_length=50)
    marca=models.CharField(null=False,max_length=50)
    precio=models.IntegerField(null=False)
