from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password','photo','nickname')


class UserSerializerView(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("photo","username","id","nickname")
