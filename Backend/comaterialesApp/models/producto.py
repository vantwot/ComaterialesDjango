from django.db import models
from .categoria import Categoria


class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(null=False, max_length=100)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fabricante =models.CharField(null=False,max_length=50, choices=(
        ('Comfort','Comfort S.A'),
        ('Decora', 'Decora S.A.S'),
        ('Multihogar', 'MultiHogar LTDA'),
        ('Corona', 'Corona S.A'),
        ('House', 'House S.A')
    ))
    marca=models.CharField(null=False,max_length=50, choices=(
        ('Arlex', 'Arlex'),
        ('Artek', 'artek'),
        ('Fatboy', 'fatboy'),
        ('Flos', 'Flos'),
        ('Vitra', 'vitra')
    ))
    precio=models.IntegerField(null=False)
