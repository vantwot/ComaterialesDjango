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
        producto = Producto.objects.get(id=obj.idProducto_id)

        return {
            'id': pedido.id,
            'idCliente': user.id,
            'idProducto': producto.id 
        }

    def crearpedido(self, validated_data):
        carrito = validated_data.pop('items')
        pedido = Pedido.objects.create(**validated_data)
        return pedido
    