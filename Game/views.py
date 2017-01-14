from django.http import *
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from Game.models import Game, Score
from Game.serializer import GameSerializer, ScoreSerializer


class GameController:
    @ensure_csrf_cookie
    @api_view(['GET', 'POST'])
    @authentication_classes([])
    @permission_classes([])
    def get(request):
        if request.method == 'GET':
            games = Game.objects.all()
            serializer = GameSerializer(games, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'POST':
            serializer = GameSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @ensure_csrf_cookie
    @api_view(['GET', 'DELETE', 'PUT'])
    @authentication_classes((TokenAuthentication,))
    def get_put_delete_game(request, pk):
        game = GameController.get_object(pk)
        if request.method == 'GET':
            serializer = GameSerializer(game)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'DELETE':
            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        if request.method == 'PUT':
            serializer = GameSerializer(game, data=request.data)
            if serializer.is_valid():
                g = Game.objects.get(pk=serializer.initial_data['id'])
                g.title = serializer.initial_data['title']
                g.description = serializer.initial_data['description']
                g.platform = serializer.initial_data['platform']
                g.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @ensure_csrf_cookie
    @api_view(['POST'])
    @authentication_classes((TokenAuthentication,))
    def add_grade(request, pk):
        try:
            data = request.data
        except ParseError as error:
            return Response(
                'Invalid JSON - {0}'.format(error.detail),
                status=status.HTTP_400_BAD_REQUEST
            )
        rec = Score.objects.filter(user_id=data['user_id'], score=data['score'])
        if len(rec) > 0:
            return Response({'message': 'Cannot score a game multiple times'}, status=status.HTTP_409_CONFLICT)
        serializer = ScoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def get_object(pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404
