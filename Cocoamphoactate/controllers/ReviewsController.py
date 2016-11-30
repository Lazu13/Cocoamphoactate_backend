from django.http import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers import *


class ReviewsController:
    @api_view(['GET', 'POST'])
    def get(request):
        if request.method == 'GET':
            reviews = Reviews.objects.all()
            serializer = ReviewsSerializer(reviews, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            serializer = ReviewsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'DELETE', 'PUT'])
    def get_put_delete_review(request, pk):
        review = ReviewsSerializer.get_object(pk)
        if request.method == 'GET':
            serializer = ReviewsSerializer(review)
            return Response(serializer.data)
        if request.method == 'DELETE':
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        if request.method == 'PUT':
            serializer = ReviewsSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_object(pk):
        try:
            return Reviews.objects.get(pk=pk)
        except Reviews.DoesNotExist:
            raise Http404
