from django.http import *
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from ..serializers import *


class GameController:
    @api_view(['GET', 'POST'])
    @authentication_classes((TokenAuthentication,))
    def get(request):
        if request.method == 'GET':
            games = Game.objects.all()
            serializer = GameSerializer(games, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            serializer = GameSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'DELETE', 'PUT'])
    @authentication_classes((TokenAuthentication,))
    def get_put_delete_game(request, pk):
        game = GameController.get_object(pk)
        if request.method == 'GET':
            serializer = GameSerializer(game)
            return Response(serializer.data)
        if request.method == 'DELETE':
            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        if request.method == 'PUT':
            serializer = GameSerializer(game, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
