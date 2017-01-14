from datetime import datetime

from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from rest_framework.authtoken.models import Token

from FriendsPending.models import FriendsPending


class FriendsPendingRestTests(TestCase):
    @classmethod
    def setUpClass(cls):
        User(id=1, username="restUser1", password="restPassword1").save()
        User(id=2, username="restUser2", password="restPassword2").save()
        Token(user_id=1, created=datetime.now(), key="testToken1").save()
        Token(user_id=2, created=datetime.now(), key="testToken2").save()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.client = Client()
        FriendsPending.objects.all().delete()

    def test_should_get_empty_list(self):
        response = self.client.get("/friends/pending", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEquals(response.data, [])

    def test_should_get_list_of_all_pending_invitations(self):
        FriendsPending(user_one_id=1, user_two_id=2).save()
        response = self.client.get("/friends/pending", **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEquals(response.json()[0]['id'], 1)
        self.assertEquals(response.json()[0]['user_one'], 1)
        self.assertEquals(response.json()[0]['user_two'], 2)

    def test_should_add_new_pending_invitation(self):
        response = self.client.post("/friends/pending/add", {"user_two": 2},
                                    **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEquals(response.status_code, 202)

    def test_should_not_add_new_invite_with_non_existing_user(self):
        response = self.client.post("/friends/pending/add", {"user_two": 9999999},
                                    **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEquals(response.status_code, 400)

    def test_should_not_add_invite_to_yourself(self):
        response = self.client.post("/friends/pending/add", {"user_two": 1},
                                    **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEquals(response.status_code, 400)

    def test_should_list_invites_sent_by_me(self):
        response = self.client.post("/friends/pending/add", {"user_two": 2},
                                    **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        response = self.client.get("/friends/pending/sent",
                                   **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEquals(response.json()[0]['user_two'], 2)

    def test_should_list_invites_received(self):
        response = self.client.post("/friends/pending/add", {"user_two": 2},
                                    **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        response = self.client.get("/friends/pending/received",
                                   **{'HTTP_AUTHORIZATION': 'Token testToken2'})
        self.assertEquals(response.json()[0]['user_one'], 1)

    def test_should_accept_invite(self):
        response = self.client.post("/friends/pending/add", {"user_two": 2},
                                    **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        response = self.client.get("/friends/pending/accept/1",
                                   **{'HTTP_AUTHORIZATION': 'Token testToken2'})
        friends = self.client.get("/friends/my",
                                  **{'HTTP_AUTHORIZATION': 'Token testToken1'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(friends.json()[0]['id'], 2)

    def test_should_not_accept_non_existing_invite(self):
        response = self.client.get("/friends/pending/accept/99999",
                                   **{'HTTP_AUTHORIZATION': 'Token testToken2'})
        self.assertEquals(response.status_code, 404)
