class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title')