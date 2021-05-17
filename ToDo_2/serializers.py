from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined')


class TodoSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Todo
        fields = ('id', 'title', 'start_at', 'created_at', 'updated_at', 'user')