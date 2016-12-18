from django.http import *
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from Cocoamphoactate.controllers.ControllerUtils import Utils
from ..serializers import *


class FriendsController:
    #/friends
    @api_view(['GET'])
    @authentication_classes((TokenAuthentication,))
    def get(request):
        if request.method == 'GET':
            friends = Friends.objects.all()
            serializer = FriendsSerializer(friends, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    #/friends/my
    @api_view(['GET'])
    @authentication_classes((TokenAuthentication,))
    def get_my_friends(request):
        current_user = Utils.get_user_from_auth(request)
        friends = Friends.objects.filter(user_one=current_user.id)
        serializers = FriendsSerializer(friends, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    @staticmethod
    def get_object(pk):
        try:
            return Friends.objects.get(pk=pk)
        except Friends.DoesNotExist:
            raise Http404
