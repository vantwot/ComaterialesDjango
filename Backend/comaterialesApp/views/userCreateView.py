from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from comaterialesApp.serializers.userSerializer import UserSerializer


class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # RECORDAD QUE PARA EL FUNCIOAMIENTO DE LAS CREDENTIALS, LOS FIELDS EN EL SERIALIZADOR DEBEN CORRESPONDER CON EL JSON INGRESADO EN EL POST.
        tokenData = {"username": request.data["username"],
                    "email": request.data["email"],
                    "password": request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)