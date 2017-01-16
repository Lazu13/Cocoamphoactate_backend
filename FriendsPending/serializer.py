# friends/pending/
from rest_framework import serializers

from FriendsPending.models import FriendsPending


# friends/pending/
class FriendsPendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendsPending
        fields = '__all__'


class InviteSerilizer(serializers.Serializer):
    class Meta:
        fields = ('id', 'user_id', 'username')


class InvitesSerializer(serializers.Serializer):
    class Meta:
        model = FriendsPending
        user_two = 'user_two'
