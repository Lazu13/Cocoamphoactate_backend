from django.http import *
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from ..serializers import *


class FriendsPendingController:
    @api_view(['GET', 'POST'])
    @authentication_classes((TokenAuthentication,))
    def get(request):
        if request.method == 'GET':
            pendings = FriendsPending.objects.all()
            serializer = FriendsPendingSerializer(pendings, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            serializer = FriendsPendingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'DELETE', 'PUT'])
    @authentication_classes((TokenAuthentication,))
    def get_put_delete_firends_pending(request, pk):
        pending = FriendsPendingController.get_object(pk)
        if request.method == 'GET':
            serializer = FriendsPendingSerializer(pending)
            return Response(serializer.data)
        if request.method == 'DELETE':
            pending.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        if request.method == 'PUT':
            serializer = FriendsPendingSerializer(pending, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_object(pk):
        try:
            return FriendsPending.objects.get(pk=pk)
        except FriendsPending.DoesNotExist:
            raise Http404
