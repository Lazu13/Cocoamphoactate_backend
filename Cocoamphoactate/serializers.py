from rest_framework import serializers

from .models import *


# users/
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


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


class MyFriendsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


# favorites/
class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'


# friends/pending/
class FriendsPendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendsPending
        fields = '__all__'


class InvitesSerializer(serializers.Serializer):
    class Meta:
        model = FriendsPending
        user_two = 'user_two'


class InviteSerilizer(serializers.Serializer):
    class Meta:
        fields = ('id', 'user_id', 'username')


# gamelib/
class GameLibSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'


# reviews/
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('game', 'review')


# score/
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title')
