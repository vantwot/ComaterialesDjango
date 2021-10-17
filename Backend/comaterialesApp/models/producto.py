from django.db import models
from .categoria import Categoria


class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(null=False, max_length=100)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fabricante =models.CharField(null=False,max_length=50, choices=(
        ('A','Comfort S.A'),
        ('B', 'Decora S.A.S'),
        ('C', 'MultiHogar LTDA'),
        ('D', 'Corona S.A'),
        ('E', 'House S.A')
    ))
    marca=models.CharField(null=False,max_length=50, choices=(
        ('A', 'Arlex'),
        ('B', 'artek'),
        ('C', 'fatboy'),
        ('D', 'Flos'),
        ('E', 'vitra')
    ))
    precio=models.IntegerField(null=False)
