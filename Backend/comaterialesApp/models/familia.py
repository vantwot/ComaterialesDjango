from django.db import models

class Familia(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(null=False, max_length = 100,choices=(
        ('A','comodidad'),
        ('B', 'natural'),
        ('C' 'ecologico'),
        ('D', 'Linea blanca')
    ))
    description=models.TextField(null=True)