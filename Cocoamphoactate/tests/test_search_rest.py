from datetime import datetime

from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from rest_framework.authtoken.models import Token

from Cocoamphoactate.models import Game


class SearchRestTests(TestCase):
    def setUp(self):
        self.client = Client()
        User(id=1, username="restUser1", password="restPassword1").save()
        Token(user_id=1, created=datetime.now(), key="testToken1").save()
        Game(title="Test Title", description="Test description", platform="PC").save()
        User(username="Test Login", password="Test pass", email="ss@ss.ss").save()

    def test_happy_path(self):
        response = self.client.post("/users/games/search", {'substring': 'Test'})
        self.assertEquals(response.status_code, 200)

    def test_should_find_game_by_substring(self):
        response = self.client.post("/users/games/search", {'substring': 'Test'})
        self.assertIn("Test Title", response.json()[0]['title'])

    def test_should_find_game_by_substring_case_insensitive(self):
        response = self.client.post("/users/games/search", {'substring': 'test'})
        self.assertIn("Test Title", response.json()[0]['title'])

    def test_should_not_find_game(self):
        response = self.client.post("/users/games/search", {'substring': 'rdaasadsaavczvcxvv'})
        self.assertEquals(response.data, [])

    def user_test_happy_path(self):
        response = self.client.post("/users/users/search", {'substring': 'Test'})
        self.assertEquals(response.status_code, 200)

    def test_should_find_user_by_substring(self):
        response = self.client.post("/users/users/search", {'substring': 'Test'})
        self.assertIn("Test Login", response.json()[0]['username'])

    def test_should_find_user_by_substring_case_insensitive(self):
        response = self.client.post("/users/users/search", {'substring': 'test'})
        self.assertIn("Test Login", response.json()[0]['username'])

    def test_should_not_find_user(self):
        response = self.client.post("/users/users/search", {'substring': 'rdaasadsaavczvcxvv'})
        self.assertEquals(response.data, [])
