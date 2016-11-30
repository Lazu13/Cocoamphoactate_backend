from rest_framework import serializers

from .models import *


# users/
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


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


# favorites/
class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'


# friends/pending/
class FriendsPendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'


# gamelib/
class GameLibSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'


# reviews/
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'