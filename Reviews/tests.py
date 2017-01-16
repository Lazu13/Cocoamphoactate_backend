from datetime import datetime

from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from rest_framework.authtoken.models import Token

from Game.models import Game
from Reviews.models import Reviews


class ReviewsRestTests(TestCase):
    def setUp(self):
        self.client = Client()
        User(id=1, username="restUser1", password="restPassword1").save()
        Token(user_id=1, created=datetime.now(), key="testToken1").save()
        Game(title="testTitle", description="testDescrtiption", platform="PC").save()

    def test_should_add_new_review(self):
        response = self.client.post("/reviews/add", {"game": 1, "review": "test Review of game"},
                                    **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        game_reviews = Reviews.objects.filter(game=1)
        self.assertEqual(len(game_reviews), 1)

    def test_should_get_all_reviews_for_game(self):
        Reviews(user_id=1, game_id=1, review="test Review").save()
        response = self.client.get("/reviews/1", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.json()[0]["review"], "test Review")

    def test_should_remove_review(self):
        Reviews(user_id=1, game_id=1, review="test Review").save()
        response = self.client.delete("/reviews/remove/1", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        reviews = Reviews.objects.filter(game=1)
        self.assertEqual(len(reviews), 0)

    def test_should_not_remove_not_existing_review(self):
        response = self.client.delete("/reviews/remove/1", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.status_code, 404)

    def test_should_not_add_review_to_not_existing_game(self):
        response = self.client.post("/reviews/add", {"game": 9999, "review": "test Review of game"},
                                    **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.status_code, 400)
