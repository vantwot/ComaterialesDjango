from rest_framework import status, views, generics
from rest_framework.response import Response
from comaterialesApp.serializers.categoriaSerializer import CategoriaSerializer
from comaterialesApp.models.categoria import Categoria

class categorias(views.APIView):
    def get(self, request, format=None): 
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

