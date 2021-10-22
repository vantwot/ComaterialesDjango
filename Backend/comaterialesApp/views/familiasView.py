from rest_framework import status, views, generics
from rest_framework.response import Response
from comaterialesApp.serializers.familiaSerializer import FamiliaSerializer
from comaterialesApp.models.familia import Familia

class familias(views.APIView):
    def get(self, request, format=None): 
        familias = Familia.objects.all()
        serializer = FamiliaSerializer(familias, many=True)
        return Response(serializer.data)
