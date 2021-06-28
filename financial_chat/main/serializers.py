from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class MessageSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class MessageSerializerList(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = '__all__'

