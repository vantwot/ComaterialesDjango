from rest_framework import serializers
from comaterialesApp.models.tipo import Tipo

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['id', 'familia', 'producto']