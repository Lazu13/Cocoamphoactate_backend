# gamelib/
class GameLibSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameLib
        fields = '__all__'