from rest_framework import status, views, generics
from rest_framework.response import Response
from comaterialesApp.serializers.pedidoSerializer import PedidoSerializer
from comaterialesApp.models.pedido import Pedido
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

"""class pedidos(views.APIView):
    autenticacion = [authentication.TokenAuthentication]
    def get(self, request, format=None): 
        
        return Response(serializer.data)
"""