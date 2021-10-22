from rest_framework import status, views, generics
from rest_framework.response import Response
from comaterialesApp.serializers.pedidoSerializer import PedidoSerializer
from comaterialesApp.models.pedido import Pedido

class pedidos(views.APIView):
    def get(self, request, format=None): 
        
        return Response(serializer.data)
