from django.test import TestCase
from ..recommendation_engine.recommendations import Engine, FRIENDS_ONLY, ALL_USERS


class engine_test_case(TestCase):
    def setUp(self):
        self.engine = Engine()

    def test_engine_add_user_throws_exception(self):
        with self.assertRaises(ValueError):
            self.engine.set_user(-1)
