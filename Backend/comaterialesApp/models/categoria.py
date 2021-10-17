from django.db import models

class Categoria(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(null=False, max_length=100 ,choices=(
        ('A', 'salas'),
        ('B', 'cocinas'),
        ('C', 'baños'),
        ('D', 'habitacion'),
        ('E','decoracion' )
    ))
    description=models.TextField(null=True)