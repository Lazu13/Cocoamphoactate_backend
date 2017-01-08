from django.test import TestCase
from ..recommendation_engine.recommendations import Engine, FRIENDS_ONLY, ALL_USERS
from rest_framework.authtoken.models import Token
from django.test import Client
from ..controllers import RecommendationController
from ..models import User, Score, Game
from datetime import datetime


class EngineTestCase(TestCase):
    def setUp(self):
        self.engine = Engine()
        self.client = Client()
        self.user = User.objects.create(id=1, username="restUser", password="restPassword")
        self.token = Token.objects.create(user_id=1, created=datetime.now(), key="testToken")

        # Prepare test data

        self.u1 = User.objects.create(username='test1', first_name='test', last_name='test', email='test@test.com',
                                      password='testpass')
        self.u2 = User.objects.create(username='test2', first_name='test', last_name='test', email='test@test.com')
        self.u3 = User.objects.create(username='test3', first_name='test', last_name='test', email='test@test.com')
        self.u4 = User.objects.create(username='test4', first_name='test', last_name='test', email='test@test.com')

        self.g1 = Game.objects.create(title='test1', description='test', platform='PC')
        self.g2 = Game.objects.create(title='test2', description='test', platform='PC')
        self.g3 = Game.objects.create(title='test3', description='test', platform='PC')
        self.g4 = Game.objects.create(title='test4', description='test', platform='PC')
        self.g5 = Game.objects.create(title='test5', description='test', platform='PC')
        self.g6 = Game.objects.create(title='test6', description='test', platform='PC')
        self.g7 = Game.objects.create(title='test7', description='test', platform='PC')
        self.g8 = Game.objects.create(title='test8', description='test', platform='PC')

        Score.objects.create(game_id=self.g1, user_id=self.u1, score=1)
        Score.objects.create(game_id=self.g1, user_id=self.u3, score=2)
        # game 1 average: 1.5

        Score.objects.create(game_id=self.g2, user_id=self.u2, score=2)
        Score.objects.create(game_id=self.g2, user_id=self.u3, score=3)
        Score.objects.create(game_id=self.g2, user_id=self.u4, score=4)
        # game 2 average: 3

        Score.objects.create(game_id=self.g3, user_id=self.u2, score=4)
        Score.objects.create(game_id=self.g3, user_id=self.user, score=5)
        #game 3 average: 4.5

        Score.objects.create(game_id=self.g4, user_id=self.u1, score=4)
        Score.objects.create(game_id=self.g4, user_id=self.u2, score=3)
        Score.objects.create(game_id=self.g4, user_id=self.u3, score=4)
        # game 4 average: 4

        Score.objects.create(game_id=self.g5, user_id=self.u4, score=3)
        Score.objects.create(game_id=self.g5, user_id=self.u2, score=3)
        # game 5 average: 3

        Score.objects.create(game_id=self.g6, user_id=self.u1, score=2)
        Score.objects.create(game_id=self.g6, user_id=self.u2, score=3)
        Score.objects.create(game_id=self.g6, user_id=self.u3, score=4)
        Score.objects.create(game_id=self.g6, user_id=self.u4, score=5)
        Score.objects.create(game_id=self.g6, user_id=self.user, score=4)
        #game 6 average: 3.60

        Score.objects.create(game_id=self.g7, user_id=self.u2, score=3)
        Score.objects.create(game_id=self.g7, user_id=self.u2, score=5)
        Score.objects.create(game_id=self.g7, user_id=self.user, score=5)
        # game 7 average: 13/3

        Score.objects.create(game_id=self.g8, user_id=self.u1, score=5)
        Score.objects.create(game_id=self.g8, user_id=self.u2, score=4)
        Score.objects.create(game_id=self.g8, user_id=self.u4, score=5)
        Score.objects.create(game_id=self.g8, user_id=self.user, score=5)
        # game 8 average: 4.75

    def test_engine_init(self):
        self.assertEqual(self.engine.type, ALL_USERS)
        self.assertIsNone(self.engine.user)

    def test_engine_set_user_throws_exception(self):
        with self.assertRaises(ValueError):
            self.engine.set_user(-1)

        with self.assertRaises(TypeError):
            self.engine.set_user("1")

    def test_engine_set_user(self):
        self.engine.set_user(1)
        self.assertEqual(self.engine.user, 1)

    def test_engine_set_type_throws_exception(self):
        with self.assertRaises(ValueError):
            self.engine.set_type(-1)

    def test_engine_set_type(self):
        self.engine.set_type(FRIENDS_ONLY)
        self.assertEqual(self.engine.type, FRIENDS_ONLY)

    def test_engine_get_best_matching_throws_exception(self):
        with self.assertRaises(User.DoesNotExist):
            eng = Engine()
            eng.get_best_matching()

    def test_engine_get_most_popular(self):
        res = self.engine.get_most_popular()
        act = [(8, 4.75), (3, 4.5), (7, 13 / 3)]
        self.assertTrue(res == dict(act))

    def test_recommendation_controller_get_most_popular(self):
        response = self.client.get('/users/recommend/mostPopular',
                                   **{'HTTP_AUTHORIZATION': 'Token testToken'})
        self.assertEqual(response.status_code, 200)

    def test_recommendation_controller_get_best_matching(self):
        response = self.client.get('/users/recommend/type/0',
                                   **{'HTTP_AUTHORIZATION': 'Token testToken'})
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/users/recommend/type/1',
                                   **{'HTTP_AUTHORIZATION': 'Token testToken'})
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/users/recommend/type/2',
                                   **{'HTTP_AUTHORIZATION': 'Token testToken'})
        self.assertEqual(response.status_code, 400)
        response = self.client.get('/users/recommend/type/3',
                                   **{'HTTP_AUTHORIZATION': 'Token testToken'})
        self.assertEqual(response.status_code, 404)

    def test_engine_pearson_algorithm(self):
        preferences = {
            1: {1: 5, 2: 5, 3: 1},
            2: {1: 1, 2: 2},
            3: {1: 3, 2: 3, 3: 3},
            4: {1: 1, 2: 1, 3: 5},
            5: {1: 5, 2: 5, 3: 1}
        }
        res = self.engine.pearson(preferences, 1, 5)
        res2 = self.engine.pearson(preferences, 1, 4)
        res3 = self.engine.pearson(preferences, 3, 1)
        self.assertAlmostEqual(res, 1.0)
        self.assertAlmostEqual(res2, -1.0)
        self.assertAlmostEqual(res3, 0.0)

    def test_engine_get_best_matching(self):
        self.engine.set_user(self.user.id)
        
        res = self.engine.get_best_matching()
        self.assertEqual(list(res.keys()), [2, 4, 5])

        self.engine.set_type(FRIENDS_ONLY)
        res = self.engine.get_best_matching()
        self.assertEqual(list(res.keys())   , [8, 3, 7])
