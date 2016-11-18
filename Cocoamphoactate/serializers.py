from rest_framework import serializers
from .models import *


# users/
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# games/
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


# friends/
class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'
