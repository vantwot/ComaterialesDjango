from rest_framework import serializers
from comaterialesApp.models.user import User

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['id','username','type_document','document','name','email','password']



    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'type_document': user.type_document,
            'document': user.document,
            'name': user.name,
            'email': user.email,
            'password':user.password 
        }