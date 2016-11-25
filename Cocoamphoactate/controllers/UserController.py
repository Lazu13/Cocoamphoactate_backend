from django.http import *
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from ..serializers import *


class UserController:
    @api_view(['POST'])
    def loginUser(request):
        if request.method == 'POST':
            serializer = LoginSerializer(data=request.data)
            print(serializer)
            serializer.is_valid()
            user = User.objects.get(username=serializer.data.get("username"), password=serializer.data.get("password"))
            print(user)
            if not user:
                return Response(
                    'No default user, please create one',
                    status=status.HTTP_404_NOT_FOUND
                )
            token = Token.objects.get_or_create(user=user)
            return Response({'detail': 'POST answer', 'token': token[0].key})
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'POST'])
    @authentication_classes((TokenAuthentication, ))
    def get(request):
        if request.method == 'GET':
            # if "user" not in request.data or "password" not in request.data:
            #     return Response(
            #         'Wrong credentials',
            #         status=status.HTTP_401_UNAUTHORIZED
            #     )
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            try:
                data = request.data
            except ParseError as error:
                return Response(
                    'Invalid JSON - {0}'.format(error.detail),
                    status=status.HTTP_400_BAD_REQUEST
                )
            # if "user" not in data or "password" not in data:
            #     return Response(
            #         'Wrong credentials',
            #         status=status.HTTP_401_UNAUTHORIZED
            #     )
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            user = User.objects.get(username=serializer.data.get("username"))
            if not user:
                return Response(
                    'No default user, please create one',
                    status=status.HTTP_404_NOT_FOUND
                )
            token = Token.objects.get_or_create(user=user)
            return Response({'detail': 'POST answer', 'token': token[0].key})

    @api_view(['GET', 'DELETE', 'PUT'])
    def get_put_delete_user(request, pk):
        user = UserController.get_object(pk)
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
