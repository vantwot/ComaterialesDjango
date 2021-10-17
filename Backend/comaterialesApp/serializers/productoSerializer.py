from rest_framework import serializers
from comaterialesApp.models.producto import Producto
from comaterialesApp.models.categoria import Categoria



class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'categoria', 'fabricante', 'marca', 'precio']

    def to_representation(self, obj):
        producto = Producto.objects.get(id=obj.id)
        categoria = Categoria.objects.get(id=obj.id)
        return {
            'id': Producto.id,
            'nombre': Producto.nombre,
            'categoria':Categoria.nombre,
            'fabricante': Producto.fabricante,
            'marca': Producto.marca,
            'precio': Producto.precio
        }