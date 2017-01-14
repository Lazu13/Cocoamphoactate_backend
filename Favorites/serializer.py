# favorites/
from rest_framework import serializers

from Favorites.models import Favorites


# favorites/
class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'
