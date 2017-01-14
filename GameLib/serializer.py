from rest_framework import serializers

from GameLib.models import GameLib


# gamelib/
class GameLibSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameLib
        fields = '__all__'
