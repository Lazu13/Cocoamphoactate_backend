from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie

from Cocoamphoactate.controllers.ControllerUtils import Utils
from ..serializers import *


class UserController:
    # users/login
    @ensure_csrf_cookie
    @api_view(['POST'])
    @authentication_classes([])
    @permission_classes([])
    def login_user(request):
        if request.method == 'POST':
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid()
            try:
                user = User.objects.get(username=serializer.data.get("username"),
                                        password=serializer.data.get("password"))
            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

            if not user:
                return Response(
                    'No default user, please create one',
                    status=status.HTTP_404_NOT_FOUND
                )
            token = Token.objects.get_or_create(user=user)
            return Response({'token': token[0].key})
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # users
    @ensure_csrf_cookie
    @api_view(['GET'])
    @authentication_classes((TokenAuthentication,))
    def get_users(request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    # users/register
    @ensure_csrf_cookie
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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

    # users/{userId}
    @ensure_csrf_cookie
    @api_view(['GET'])
    @authentication_classes((TokenAuthentication,))
    def get_user(request, pk):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response("Given user does not exisit", status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # user
    @ensure_csrf_cookie
    @api_view(['GET', 'DELETE', 'PUT'])
    @authentication_classes((TokenAuthentication,))
    def get_put_delete_user(request):
        try:
            user = Utils.get_user_from_auth(request)
        except [ValueError, User.DoesNotExist] as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
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
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
