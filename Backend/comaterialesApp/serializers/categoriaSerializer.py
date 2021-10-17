from rest_framework import serializers
from comaterialesApp.models.categoria import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        #QUE MODELO QUEREMOS SERIALIZAR ? ->
        model = Categoria # PONEMOS EL MODELO QUE QUEREMOS SERIALIZAR
        fields = ['id','nombre','description'] # CAMPOS QUE TIENE EL MODELO, QUE QUEREMOS SERIALIZAR