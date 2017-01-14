from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from Game.models import Game
from Game.serializer import GameSerializer
from Search.serializer import SearchSerializer
from Users.serializer import UserSerializer


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

    @ensure_csrf_cookie
    @api_view(['POST'])
    @authentication_classes([])
    @permission_classes([])
    def search_users(request):
        searchedPhrase = SearchSerializer(data=request.data)
        searchedPhrase.is_valid()
        users = User.objects.filter(username__contains=searchedPhrase.initial_data.get("substring"))
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
