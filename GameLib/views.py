from django.http import *
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from Cocoamphoactate.ControllerUtils import Utils
from GameLib.models import GameLib
from GameLib.serializer import GameLibSerializer


class GameLibController:
    @ensure_csrf_cookie
    @api_view(['GET', 'POST'])
    @authentication_classes((TokenAuthentication,))
    def get(request):
        current_user = Utils.get_user_from_auth(request)
        if request.method == 'GET':
            libs = GameLib.objects.filter(user=current_user.id)
            serializer = GameLibSerializer(libs, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            serializer = GameLibSerializer(data=request.data)
            if serializer.is_valid():
                user_game = GameLib.objects.filter(user=current_user.id, game=request.data['game'])
                if len(user_game)>0:
                    return Response("Cannot add twice", status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @ensure_csrf_cookie
    @api_view(['DELETE'])
    @authentication_classes((TokenAuthentication,))
    def get_put_delete_lib(request, pk):
        lib = GameLibController.get_object(pk)
        if request.method == 'DELETE':
            lib.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def get_object(pk):
        try:
            return GameLib.objects.get(pk=pk)
        except GameLib.DoesNotExist:
            raise Http404
