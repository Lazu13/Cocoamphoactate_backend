# score/
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'

# games/
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'