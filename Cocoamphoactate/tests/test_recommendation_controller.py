from django.test import TestCase
from ..recommendation_engine.recommendations import Engine, FRIENDS_ONLY, ALL_USERS
from ..controllers.RecommendationController import RecommendationController


class RecommendationControllerTestCase(TestCase):
    def setUP(self):
        self.controller = RecommendationController()

    def test_get_most_popular(self):
        self.assertTrue(True)