from django.db import models

class Categoria(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(null=False, max_length=100 ,choices=(
        ('Salas', 'salas'),
        ('Cocinas', 'cocinas'),
        ('Baños', 'baños'),
        ('Habitación', 'habitacion'),
        ('Decoración','decoracion' )
    ))
    description=models.TextField(null=True)