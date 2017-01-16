from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from Cocoamphoactate.ControllerUtils import Utils
from Recommendation.recommendations import Engine
from Game.models import Game


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
            games = engine.get_best_matching()
            data = []
            for g in games.keys():
                game = Game.objects.filter(id=g)[0]
                dat = {"id": game.id,
                       "title": game.title,
                       "description": game.description,
                       "platform": game.platform,
                       "score": games[g],
                       "url": game.url}
                data.append(dat)
        except ValueError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except TypeError as e:

            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)

    @api_view(['GET'])
    @ensure_csrf_cookie
    @authentication_classes([])
    @permission_classes([])
    def get_most_popular(request):
        engine = Engine()
        games = engine.get_most_popular()
        data = []
        for g in games.keys():
            game = Game.objects.filter(id=g)[0]
            dat = {"id": game.id,
                   "title": game.title,
                   "description": game.description,
                   "platform": game.platform,
                   "score": games[g],
                   "url": game.url}
            data.append(dat)
        return Response(data, status=status.HTTP_200_OK)
