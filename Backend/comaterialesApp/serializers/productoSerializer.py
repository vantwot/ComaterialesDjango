from rest_framework import serializers
from comaterialesApp.models.producto import Producto
from comaterialesApp.models.categoria import Categoria



class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'categoria', 'fabricante', 'marca', 'precio']


    def to_representation(self, obj):
        producto = Producto.objects.get(id=obj.id)
        categoria = Categoria.objects.get(id=obj.categoria_id)
        return {
            'id': producto.id,
            'nombre': producto.nombre,
            'categoria':categoria.nombre,
            'fabricante': producto.fabricante,
            'marca': producto.marca,
            'precio': producto.precio
        }
