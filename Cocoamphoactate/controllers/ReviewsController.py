from django.http import *
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from Cocoamphoactate.controllers.ControllerUtils import Utils
from ..serializers import *


class ReviewsController:
    @ensure_csrf_cookie
    @api_view(['POST'])
    @authentication_classes((TokenAuthentication,))
    def post_game_review(request):
        current_user = Utils.get_user_from_auth(request=request)
        if request.method == 'POST':
            serializer = ReviewsSerializer(data=request.data)
            if serializer.is_valid():
                review = Reviews(user=current_user, game_id=serializer.data["game"], review=serializer.data["review"])
                review.save()
                return Response("Review saved successfully", status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @ensure_csrf_cookie
    @api_view(['GET'])
    @authentication_classes((TokenAuthentication,))
    def get_game_reviews(request, pk):
        if request.method == 'GET':
            reviews = Reviews.objects.filter(game=pk)
            serializer = ReviewsSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @ensure_csrf_cookie
    @api_view(['DELETE'])
    @authentication_classes((TokenAuthentication,))
    def remove_review(request, pk):
        if request.method == 'DELETE':
            try:
                reviews = Reviews.objects.get(pk=pk)
                reviews.delete()
            except Reviews.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(status=status.HTTP_200_OK)

    @staticmethod
    def get_object(pk):
        try:
            return Reviews.objects.get(pk=pk)
        except Reviews.DoesNotExist:
            raise Http404
