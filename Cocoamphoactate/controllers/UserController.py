from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from Cocoamphoactate.controllers.ControllerUtils import Utils
from ..serializers import *


class UserController:
    @api_view(['POST'])
    def login_user(request):
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

    @api_view(['GET'])
    @authentication_classes((TokenAuthentication,))
    def get_users(request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @api_view(['POST'])
    @authentication_classes([])
    @permission_classes([])
    def register(request):
        try:
            data = request.data
        except ParseError as error:
            return Response(
                'Invalid JSON - {0}'.format(error.detail),
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

    @api_view(['GET', 'DELETE', 'PUT'])
    @authentication_classes((TokenAuthentication,))
    def get_put_delete_user(request):
        try:
            user = Utils.get_user_from_auth(request)
        except [ValueError, User.DoesNotExist]:
            return Response(status=status.HTTP_400_BAD_REQUEST)
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
