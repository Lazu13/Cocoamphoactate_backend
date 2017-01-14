# reviews/
from rest_framework import serializers

from Reviews.models import Reviews


# reviews/
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('game', 'user', 'review')
