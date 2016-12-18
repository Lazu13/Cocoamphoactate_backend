from django.http import *
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie

from ..serializers import *


class GameLibController:
    @ensure_csrf_cookie
    @api_view(['GET', 'POST'])
    @authentication_classes((TokenAuthentication,))
    def get(request):
        if request.method == 'GET':
            libs = GameLib.objects.all()
            serializer = GameLibSerializer(libs, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            serializer = GameLibSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @ensure_csrf_cookie
    @api_view(['GET', 'DELETE', 'PUT'])
    @authentication_classes((TokenAuthentication,))
    def get_put_delete_lib(request, pk):
        lib = GameLibController.get_object(pk)
        if request.method == 'GET':
            serializer = GameLibSerializer(lib)
            return Response(serializer.data)
        if request.method == 'DELETE':
            lib.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        if request.method == 'PUT':
            serializer = GameLibSerializer(lib, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_object(pk):
        try:
            return GameLib.objects.get(pk=pk)
        except GameLib.DoesNotExist:
            raise Http404
