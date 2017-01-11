from datetime import datetime

from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from rest_framework.authtoken.models import Token

from Cocoamphoactate.models import FriendsPending, Friends


class FriendsRestTests(TestCase):
    def setUp(self):
        self.client = Client()
        User(id=1, username="restUser1", password="restPassword1").save()
        User(id=2, username="restUser2", password="restPassword2").save()
        Token(user_id=1, created=datetime.now(), key="testToken1").save()
        Token(user_id=2, created=datetime.now(), key="testToken2").save()
        Friends(user_one_id=1, user_two_id=2).save()

    def test_should_get_all_my_friends(self):
        response = self.client.get("/friends/my", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEqual(response.json()[0]["username"], "restUser2")

    def test_should_get_all_friends_relationships(self):
        response = self.client.get("/friends", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        friends = Friends.objects.all()
        self.assertEqual(len(friends), len(response.json()))