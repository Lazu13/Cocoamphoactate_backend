from rest_framework import serializers

from Game.models import Game


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title')
