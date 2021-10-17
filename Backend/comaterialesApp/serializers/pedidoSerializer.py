from rest_framework import serializers
from comaterialesApp.models.pedido import Pedido
from comaterialesApp.models.user import User
from comaterialesApp.models.producto import Producto

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'idCliente', 'idProducto']
    
    def to_representation(self, obj):
        pedido = Pedido.objects.get(id=obj.id)
        user  = User.objects.get(id=obj.id)
        producto = Producto.objects.get(id=obj.id)

        return {
            'id': Pedido.id,
            'idCliente': User.id,
            'idProducto': Producto.id 
        }
