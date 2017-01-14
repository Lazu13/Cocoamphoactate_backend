from django.http import *
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie

from Cocoamphoactate.controllers.ControllerUtils import Utils
from ..serializers import *


class FavoritesController:
    @ensure_csrf_cookie
    @api_view(['GET', 'POST'])
    @authentication_classes((TokenAuthentication,))
    def get(request):
        current_user = Utils.get_user_from_auth(request)
        if request.method == 'GET':
            favs = Favorites.objects.filter(user=current_user.id)
            serializer = FavoritesSerializer(favs, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            data = request.data
            data.update({"user": current_user.id})
            serializer = FavoritesSerializer(data=data)
            if serializer.is_valid():
                fav = Favorites.objects.filter(user=current_user.id, game=request.data['game'])
                if len(fav) > 0:
                    return Response("Cannot add twice", status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @ensure_csrf_cookie
    @api_view(['DELETE'])
    @authentication_classes((TokenAuthentication,))
    def remove_favorite(request, pk):
        fav = FavoritesController.get_object(pk, Utils.get_user_from_auth(request))
        if request.method == 'DELETE':
            fav.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def get_object(pk, user):
        try:
            return Favorites.objects.get(game=pk, user=user)
        except Favorites.DoesNotExist:
            raise Http404
