from django.contrib.auth.models import User
from django.http import *
from django.views.decorators.csrf import ensure_csrf_cookie
from django.db.models import Q
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from Cocoamphoactate.ControllerUtils import Utils
from Friends.models import Friends
from Friends.serializer import FriendsSerializer, MyFriendsSerilizer


class FriendsController:
    # /friends
    @ensure_csrf_cookie
    @api_view(['GET'])
    @authentication_classes((TokenAuthentication,))
    def get(request):
        if request.method == 'GET':
            friends = Friends.objects.all()
            serializer = FriendsSerializer(friends, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # /friends/my
    @ensure_csrf_cookie
    @api_view(['GET'])
    @authentication_classes((TokenAuthentication,))
    def get_my_friends(request):
        current_user = Utils.get_user_from_auth(request)
        friends = Friends.objects.filter(Q(user_one=current_user.id) | Q(user_two=current_user.id))
        users = []
        for friend in friends:
            if friend.user_two_id == current_user.id:
                id = friend.user_one_id
            else:
                id = friend.user_two_id
            users.append(User.objects.get(id=id))
        serializers = MyFriendsSerilizer(users, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
