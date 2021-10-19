from rest_framework import status, views, generics
from rest_framework.response import Response
from comaterialesApp.serializers.productoSerializer import ProductoSerializer
from comaterialesApp.models.producto import Producto



class productos(views.APIView):
    def get(self, request, format=None):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
"""

class productos(generics.ListAPIView):
    serializer_class = ProductoSerializer
    def get_queryset(self):
        queryset = Producto.objects.all()
        return queryset
"""