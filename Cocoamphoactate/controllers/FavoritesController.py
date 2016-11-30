from django.http import *
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from ..serializers import *


class FavoritesController:
    @api_view(['GET', 'POST'])
    @authentication_classes((TokenAuthentication,))
    def get(request):
        if request.method == 'GET':
            favs = Favorites.objects.all()
            serializer = FavoritesSerializer(favs, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            serializer = FavoritesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'DELETE', 'PUT'])
    @authentication_classes((TokenAuthentication,))
    def get_put_delete_favorite(request, pk):
        fav = FavoritesController.get_object(pk)
        if request.method == 'GET':
            serializer = FavoritesSerializer(fav)
            return Response(serializer.data)
        if request.method == 'DELETE':
            fav.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        if request.method == 'PUT':
            serializer = FavoritesSerializer(fav, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_object(pk):
        try:
            return Favorites.objects.get(pk=pk)
        except Favorites.DoesNotExist:
            raise Http404
