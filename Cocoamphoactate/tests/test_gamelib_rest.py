from datetime import datetime

from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from rest_framework.authtoken.models import Token

from Cocoamphoactate.models import Game, GameLib


class GameLibRestTests(TestCase):
    def setUp(self):
        self.client = Client()
        User(id=1, username="restUser1", password="restPassword1").save()
        Token(user_id=1, created=datetime.now(), key="testToken1").save()
        Game(title="testTitle", description="testDescrtiption", platform="PC").save()

    def test_should_add_to_gamelib(self):
        response = self.client.post("/gamelib", {"user": 1, "game": 1}, **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        user_games = GameLib.objects.filter(user=1)
        self.assertEqual(len(user_games), 1)

    def test_should_remove_from_gamelib(self):
        GameLib(user_id=1, game_id=1).save()
        response = self.client.delete("/gamelib/1", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        user_games = GameLib.objects.filter(user=1)
        self.assertEqual(len(user_games), 0)

    def test_should_not_add_twice(self):
        GameLib(user_id=1, game_id=1).save()
        response = self.client.post("/gamelib", {"user": 1, "game": 1}, **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.status_code, 400)

    def test_should_not_remove_not_existing_game_from_gamelb(self):
        response = self.client.delete("/gamelib/1", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.status_code, 404)

    def test_should_not_add_not_existing_game_to_gamelib(self):
        response = self.client.post("/gamelib", {"user": 1, "game": 999}, **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.status_code, 400)
