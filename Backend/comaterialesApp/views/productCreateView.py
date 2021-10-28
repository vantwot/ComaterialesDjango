from django.conf import settings
from django.db.models.query import QuerySet # configuracion del proyecto 
from rest_framework import generics,status, views # LIBRERIA para hacer el crud 
from rest_framework.response import Response # hacer un response de alguna data , mensaje, etc..
from rest_framework.permissions import IsAdminUser, IsAuthenticated # para comprobar si un modelo está autenticado y poder hacer su respectivo uso 
from rest_framework_simplejwt.backends import TokenBackend # para validacion de token
from comaterialesApp.serializers.productoSerializer import ProductoSerializer
from comaterialesApp.models.producto import Producto

class productos(views.APIView):
    def get(self, request, format=None):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

class productoDetailView(generics.ListAPIView): # retrieve es para traer la informacion
    serializer_class = ProductoSerializer
    def get_queryset(self):     
        queryset = Producto.objects.filter(id = self.kwargs['pk'])
        return queryset
        
"""
class productos(generics.ListAPIView):
    serializer_class = ProductoSerializer
    def get_queryset(self):
        queryset = Producto.objects.all()
        return queryset
"""