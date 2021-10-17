from django.db import models

class Categoria(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.TextField(null=False)
    description=models.TextField(null=True)