from django.http import *
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie

from Cocoamphoactate.controllers.ControllerUtils import Utils
from ..serializers import *


class FriendsPendingController:
    # friends/pending
    @ensure_csrf_cookie
    @api_view(['GET'])
    @authentication_classes((TokenAuthentication,))
    def get_all_pending_ivites(request):
        pendings = FriendsPending.objects.all()
        serializer = FriendsPendingSerializer(pendings, many=True)
        return Response(serializer.data)

    # friends/pending/sent
    @ensure_csrf_cookie
    @api_view(['GET'])
    @authentication_classes((TokenAuthentication,))
    def get_sent_by_me(request):
        current_user = Utils.get_user_from_auth(request)
        sent = FriendsPending.objects.filter(user_one=current_user.id)
        serializer = FriendsPendingSerializer(sent, many=True)
        return Response(serializer.data)

    # friends/pending/received
    @ensure_csrf_cookie
    @api_view(['GET'])
    @authentication_classes((TokenAuthentication,))
    def get_received(request):
        current_user = Utils.get_user_from_auth(request)
        sent = FriendsPending.objects.filter(user_two=current_user.id)
        serializer = FriendsPendingSerializer(sent, many=True)
        return Response(serializer.data)

    # friends/pending/add
    @ensure_csrf_cookie
    @api_view(['POST'])
    @authentication_classes((TokenAuthentication,))
    def invite_user(request):
        current_user = Utils.get_user_from_auth(request)
        data = request.data
        data.update({"user": current_user.id})
        serializer = InvitesSerializer(data=data)
        if serializer.is_valid():
            init_data = int(serializer.initial_data["user_two"])
            flag = False
            try:
                User.objects.get(id=init_data)
            except User.DoesNotExist:
                return Response("Cannot invite non existing user", status=status.HTTP_400_BAD_REQUEST)
            if current_user.id == init_data:
                return Response("Cannot send invite to yourself", status=status.HTTP_400_BAD_REQUEST)
            try:
                friends = Friends.objects.get(user_one_id=current_user.id, user_two_id=init_data)
                return Response("Cannot invite user. Already friend", status=status.HTTP_400_BAD_REQUEST)
            except Friends.DoesNotExist:
                pass
            try:
                friends = Friends.objects.get(user_one_id=init_data, user_two_id=current_user.id)
                return Response("Cannot invite user. Already friend", status=status.HTTP_400_BAD_REQUEST)
            except Friends.DoesNotExist:
                pass
            invitation = FriendsPending(user_one_id=current_user.id, user_two_id=init_data)
            try:
                FriendsPending.objects.get(user_one_id=current_user, user_two_id=init_data)
                return Response("Cannot send invite twice", status=status.HTTP_400_BAD_REQUEST)
            except FriendsPending.DoesNotExist:
                pass
            try:
                FriendsPending.objects.get(user_one_id=init_data, user_two_id=current_user)
                return Response("Cannot send invite twice", status=status.HTTP_400_BAD_REQUEST)
            except FriendsPending.DoesNotExist:
                pass
            invitation.save()
            return Response(serializer.initial_data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # friends/pending/accept/{invite_id}
    @ensure_csrf_cookie
    @api_view(['GET'])
    @authentication_classes((TokenAuthentication,))
    def accept_invite(request, pk):
        current_user = Utils.get_user_from_auth(request)
        try:
            invite = FriendsPendingController.get_object(pk=pk, current_id=current_user.id)
        except FriendsPending.DoesNotExist:
            return Response("Invitation does not exist", status=status.HTTP_404_NOT_FOUND)
        friends = Friends(user_one_id=invite.user_one_id, user_two_id=invite.user_two_id)
        try:
            friends.save()
            invite.delete()
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def get_object(pk, current_id):
        try:
            return FriendsPending.objects.get(pk=pk, user_two_id=current_id)
        except FriendsPending.DoesNotExist:
            raise Http404
