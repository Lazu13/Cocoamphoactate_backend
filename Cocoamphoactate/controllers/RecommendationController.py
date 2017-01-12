from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie
from ..recommendation_engine.recommendations import Engine, ALL_USERS, FRIENDS_ONLY
from .ControllerUtils import Utils


class RecommendationController():
    @api_view(['GET'])
    @ensure_csrf_cookie
    @authentication_classes((TokenAuthentication,))
    def get(request, t):
        engine = Engine()
        try:
            user = Utils.get_user_from_auth(request)
            engine.set_user(user.id)
            engine.set_type(t)
            res = engine.get_best_matching()
        except ValueError as e:
            print(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except TypeError as e:

            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(res, status=status.HTTP_200_OK)

    @api_view(['GET'])
    @ensure_csrf_cookie
    @authentication_classes([])
    @permission_classes([])
    def get_most_popular(request):
        engine = Engine()
        games = engine.get_most_popular()
        return Response(games, status=status.HTTP_200_OK)
