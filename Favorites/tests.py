from datetime import datetime

from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from rest_framework.authtoken.models import Token

from Favorites.models import Favorites
from Game.models import Game


class FavoritesRestTests(TestCase):
    def setUp(self):
        self.client = Client()
        User(id=1, username="restUser1", password="restPassword1").save()
        Token(user_id=1, created=datetime.now(), key="testToken1").save()
        Game(title="testTitle", description="testDescrtiption", platform="PC").save()

    def test_should_get_list_of_favorites(self):
        Favorites(game_id=1, user_id=1).save()
        response = self.client.get("/favs", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.json()[0]['game'], 1)

    def test_should_add_to_favorite(self):
        response = self.client.post("/favs", {"user": 1, "game": 1}, **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        response = self.client.get("/favs", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.json()[0]['game'], 1)

    def test_should_remove_from_favorites(self):
        Favorites(game_id=1, user_id=1).save()
        response = self.client.delete("/favs/1", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(len(Favorites.objects.all()), 0)

    def test_should_not_add_twice(self):
        response = self.client.post("/favs", {"user": 1, "game": 1}, **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        response = self.client.post("/favs", {"user": 1, "game": 1}, **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.status_code, 400)

    def test_should_not_remove_not_existing(self):
        response = self.client.delete("/favs/1", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.status_code, 404)

    def test_should_not_add_not_existing_game(self):
        response = self.client.post("/favs", {"user": 1, "game": 9999}, **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.status_code, 400)
