# friends/
from django.contrib.auth.models import User
from rest_framework import serializers

from Friends.models import Friends


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'


class MyFriendsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')