from django.http import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers import *


class UserController:
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
