from django.db import models
from .user import User
from .producto import Producto

class Pedido(models.Model):
  id = models.AutoField(primary_key=True)
  idCliente = models.ForeignKey(User,on_delete=models.CASCADE)
  idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)