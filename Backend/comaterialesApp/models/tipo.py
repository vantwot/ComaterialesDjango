from django.db import models
from .familia import Familia
from .producto import Producto

class Tipo(models.Model):
    id=models.AutoField(primary_key=True)
    familia=models.ForeignKey(Familia,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
