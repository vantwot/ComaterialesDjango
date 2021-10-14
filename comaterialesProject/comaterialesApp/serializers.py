from rest_framework import serializers

from .models import Categoria, Producto

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = {
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        }