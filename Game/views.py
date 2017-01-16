from django.http import *
from django.views.decorators.csrf import ensure_csrf_cookie
from django.db.models import Avg
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from django.contrib.auth.models import User
from Game.models import Game, Score
from Game.serializer import GameSerializer, ScoreSerializer
from Cocoamphoactate.ControllerUtils import Utils


class GameController:
    @ensure_csrf_cookie
    @api_view(['GET'])
    @authentication_classes([])
    @permission_classes([])
    def get(request):
        if request.method == 'GET':
            games = Game.objects.all()
            data = []
            for game in games:
                lst = list(Score.objects.values('game_id').filter(game_id=game.id).annotate(Avg('score')))
                if len(lst) > 0:
                    avr = lst[0]['score__avg']
                else:
                    avr = 0
                dat = {"id": game.id,
                       "title": game.title,
                       "description": game.description,
                       "platform": game.platform,
                       "score": avr,
                       "url": game.url}
                data.append(dat)
            return Response(data, status=status.HTTP_200_OK)

    @ensure_csrf_cookie
    @api_view(['POST'])
    @authentication_classes((TokenAuthentication,))
    def post(request):
        if request.method == 'POST':
            user = Utils.get_user_from_auth(request)
            if not user.is_superuser:
                return Response("Not a superuser", status=status.HTTP_403_FORBIDDEN)
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
        user = Utils.get_user_from_auth(request)
        if request.method == 'GET':
            lst = list(Score.objects.values('game_id').filter(game_id=game.id).annotate(Avg('score')))
            if len(lst) > 0:
                avr = lst[0]['score__avg']
            else:
                avr = 0
            dat = {"id": game.id,
                   "title": game.title,
                   "description": game.description,
                   "platform": game.platform,
                   "score": avr,
                   "url": game.url}
            return Response(dat, status=status.HTTP_200_OK)
        if request.method == 'DELETE':
            if not user.is_superuser:
                return Response("Not a superuser", status=status.HTTP_403_FORBIDDEN)
            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        if request.method == 'PUT':
            if not user.is_superuser:
                return Response("Not a superuser", status=status.HTTP_403_FORBIDDEN)
            serializer = GameSerializer(game, data=request.data)
            if serializer.is_valid():
                g = Game.objects.get(pk=serializer.initial_data['id'])
                g.title = serializer.initial_data['title']
                g.description = serializer.initial_data['description']
                g.platform = serializer.initial_data['platform']
                g.url = serializer.initial_data['url']
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
        rec = Score.objects.filter(user_id=data['user_id'], game_id=data['game_id'])
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
