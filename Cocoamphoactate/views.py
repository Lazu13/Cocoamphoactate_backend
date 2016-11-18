from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import *
from django.http import *
from rest_framework.decorators import api_view
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser


class UserApi:
    @api_view(['GET', 'POST'])
    def get(request):
        if request.method == 'GET':
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'DELETE', 'PUT'])
    def get_put_delete_user(request, pk):
        user = UserApi.get_object(pk)
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)
        if request.method == 'DELETE':
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        if request.method == 'PUT':
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_object(pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404


class GameApi:
    @api_view(['GET', 'POST'])
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
    def get_put_delete_game(request, pk):
        game = GameApi.get_object(pk)
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

    @staticmethod
    def get_object(pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404


class FriendsApi:
    @api_view(['GET', 'POST'])
    def get(request):
        if request.method == 'GET':
            friends = Friends.objects.all()
            serializer = FriendsSerializer(friends, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            serializer = FriendsSerializer(data=request.data)
            if serializer.is_valid():
                UserApi.get_object(serializer.validated_data['user_one'].id)
                UserApi.get_object(serializer.validated_data['user_two'].id)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'DELETE', 'PUT'])
    def get_put_delete_friends(request, pk):
        friends = FriendsApi.get_object(pk)
        if request.method == 'GET':
            serializer = FriendsSerializer(friends)
            return Response(serializer.data)
        if request.method == 'DELETE':
            friends.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        if request.method == 'PUT':
            serializer = FriendsSerializer(friends, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_object(pk):
        try:
            return Friends.objects.get(pk=pk)
        except Friends.DoesNotExist:
            raise Http404
