from datetime import datetime

from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from rest_framework.authtoken.models import Token

from Game.models import Game, Score


class GameRestTests(TestCase):
    def setUp(self):
        User(id=1, username="restUser1", password="restPassword1").save()
        Token(user_id=1, created=datetime.now(), key="testToken1").save()
        self.client = Client()

    def test_should_add_new_game(self):
        response = self.client.post("/games",
                                    {'title': 'testTitle', 'description': 'testDescription', 'platform': 'PC'},
                                    **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        games = Game.objects.all()
        self.assertEqual(len(games), 1)

    def test_should_get_all_games(self):
        Game(title="testTitle", description="testDescrtiption", platform="PC").save()
        response = self.client.get("/games", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.json()[0]['title'], "testTitle")

    def test_should_get_game(self):
        Game(title="testTitle", description="testDescrtiption", platform="PC").save()
        response = self.client.get("/games/1", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.json()['title'], "testTitle")

    def test_should_edit_game(self):
        Game(title="testTitle", description="testDescrtiption", platform="PC").save()
        response = self.client.put("/games/1",
                                   '{"id":1,"title": "testTitleNew", "description": "testDescriptionNew", "platform": "PC"}',
                                   **{'HTTP_AUTHORIZATION': 'Token testToken1', 'content_type': 'application/json'})
        response = self.client.get("/games/1", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.json()['title'], "testTitleNew")

    def test_should_remove_game(self):
        Game(title="testTitle", description="testDescrtiption", platform="PC").save()
        response = self.client.delete("/games/1", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(len(Game.objects.all()), 0)

    def test_should_add_new_score(self):
        Game(title="testTitle", description="testDescrtiption", platform="PC").save()
        response = self.client.post("/games/1/grade", {"game_id": 1, "user_id": 1, "score": 5},
                                    **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        score = Score.objects.get(game_id=1)
        self.assertEqual(score.score, 5)

    def test_should_not_add_existing_game(self):
        Game(title="testTitle", description="testDescrtiption", platform="PC").save()
        response = self.client.post("/games",
                                    {'title': 'testTitle', 'description': 'testDescription', 'platform': 'PC'},
                                    **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.status_code, 400)

    def test_should_not_add_with_invalid_format(self):
        response = self.client.post("/games",
                                    {'notValid': 'testTitle', 'description': 'testDescription', 'platform': 'PC'},
                                    **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.status_code, 400)

    def test_should_not_edit_to_existing_game(self):
        Game(title="testTitle1", description="testDescrtiption", platform="PC").save()
        Game(title="testTitle2", description="testDescrtiption", platform="PC").save()
        response = self.client.put("/games/1",
                                   '{"id":1,"title": "testTitle2", "description": "testDescriptionNew", "platform": "PC"}',
                                   **{'HTTP_AUTHORIZATION': 'Token testToken1', 'content_type': 'application/json'})
        self.assertEqual(response.status_code, 400)

    def test_should_not_edit_not_existing_game(self):
        response = self.client.put("/games/1",
                                   '{"id":10000,"title": "testTitleNew", "description": "testDescriptionNew", "platform": "PC"}',
                                   **{'HTTP_AUTHORIZATION': 'Token testToken1', 'content_type': 'application/json'})
        self.assertEqual(response.status_code, 404)

    def test_should_not_remove_not_existing_game(self):
        response = self.client.delete("/games/1", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.status_code, 404)

    def test_should_not_get_not_existing_game(self):
        response = self.client.get("/games/1", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.status_code, 404)
