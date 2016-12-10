import string
from random import randint
import random

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from Cocoamphoactate.models import Friends, Game, FriendsPending, Score, GameLib, Reviews, Favorites


class DataLoader(object):

    @api_view(['GET'])
    @authentication_classes([])
    @permission_classes([])
    def get_status(request):
        dataloader = DataLoader()
        dataloader.clean_up_database()
        dataloader.put_mock_data_in_database()
        return Response("OK", status=status.HTTP_200_OK)

    def clean_up_database(self):
        Friends.objects.all().delete()
        FriendsPending.objects.all().delete()
        Score.objects.all().delete()
        GameLib.objects.all().delete()
        Reviews.objects.all().delete()
        Game.objects.all().delete()
        User.objects.all().delete()

    def put_mock_data_in_database(self):
        for i in range(1, 10):
            username = "testUSer".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
            password = "testPass".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
            user = User(id=i, username=username, password=password)
            user.save()

        for i in range(1, 10):
            title = "testTitle".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
            description = "testDesc".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
            game = Game(title=title, description=description, platform="PC")
            game.save()

        for i in range(1, 10):
            user_one = randint(1, 10)
            user_two = randint(1, 10)
            friends = Friends(user_one_id=user_one, user_two_id=user_two)
            friends.save()

        for i in range(1, 10):
            user_one = randint(1, 10)
            user_two = randint(1, 10)
            friends_pending = FriendsPending(user_one_id=user_one, user_two_id=user_two)
            friends_pending.save()

        for i in range(1, 10):
            game_id = randint(1, 10)
            user_id = randint(1, 10)
            try:
                game = Game.objects.get(pk=game_id)
            except Game.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            score = Score(game_id=game, user_id=user_id, score=4.0)
            score.save()

        for i in range(1, 10):
            user_id = randint(1, 10)
            game_id = randint(1, 10)
            favs = Favorites(user=user_id, game=game_id)
            favs.save()

        for i in range(1, 10):
            user_id = randint(1, 10)
            game_id = randint(1, 10)
            libs = GameLib(user=user_id, game=game_id)
            libs.save()

        for i in range(1, 10):
            user_id = randint(1, 10)
            game_id = randint(1, 10)
            reviews = Reviews(user=user_id, game=game_id, review="placeholder text")
            reviews.save()
