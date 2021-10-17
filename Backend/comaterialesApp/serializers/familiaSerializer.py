from rest_framework import serializers
from comaterialesApp.models.familia import Familia

class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        #QUE MODELO QUEREMOS SERIALIZAR ? ->
        model = Familia # PONEMOS EL MODELO QUE QUEREMOS SERIALIZAR
        fields = ['id','nombre','description'] # CAMPOS QUE TIENE EL MODELO, QUE QUEREMOS SERIALIZAR