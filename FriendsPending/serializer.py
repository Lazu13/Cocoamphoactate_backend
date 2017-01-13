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