from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from Cocoamphoactate.models import Game
from Cocoamphoactate.serializers import GameSerializer, SearchSerializer


class Search:
    @ensure_csrf_cookie
    @api_view(['POST'])
    @authentication_classes([])
    @permission_classes([])
    def search_games(request):
        searchedPhrase = SearchSerializer(data=request.data)
        searchedPhrase.is_valid()
        games = Game.objects.filter(title__contains=searchedPhrase.initial_data.get("substring"))
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)