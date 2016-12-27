from datetime import datetime

from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from rest_framework.authtoken.models import Token


class UserRestTests(TestCase):
    def setUp(self):
        self.client = Client()
        User(id=1, username="restUser", password="restPassword").save()
        Token(user_id=1,created=datetime.now(), key="testToken").save()

    def test_login_non_existing_user(self):
        response = self.client.post("/users/login", {'username':'non_exist', 'password':'some_pass'})
        self.failUnlessEqual(response.status_code, 400)

    def test_login_with_wrong_password(self):
        response = self.client.post("/users/login", {'username':'restUser', 'password':'some_pass'})
        self.failUnlessEqual(response.status_code, 400)

    def test_login_and_get_token(self):
        response = self.client.post("/users/login", {'username':'restUser', 'password':'restPassword'})
        self.assertEquals(response.status_code, 200)
        self.assertIn("token", response.data)

    def test_should_fail_if_user_already_exists(self):
        response = self.client.post("/users/register", {'username':'restUser', 'password':'restPassword'})
        self.assertEquals(response.status_code, 400)

    def test_should_fail_with_invalid_json_format(self):
        response = self.client.post("/users/register", {'user': 'user', 'password':'restPassword'})
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.json()['username'][0], "This field is required.")

    def test_should_fail_with_too_short_password(self):
        response = self.client.post("/users/register", {'username': 'restUser', 'password':'r'})
        self.assertEquals(response.status_code, 400)

    def test_should_fail_with_empty_password(self):
        response = self.client.post("/users/register", {'username': 'restUser', 'password': ''})
        self.assertEquals(response.status_code, 400)

    def test_should_fail_with_empty_username(self):
        response = self.client.post("/users/register", {'username': '', 'password': 'some_password'})
        self.assertEquals(response.status_code, 400)

    def test_should_properly_register(self):
        response = self.client.post("/users/register", {'username': 'newUser', 'password': 'newPassword'})
        self.assertEquals(response.status_code, 200)

    def test_should_process_authenticated_request_properly(self):
        response = self.client.get("/users",  **{'HTTP_AUTHORIZATION' : 'Token testToken'})
        self.assertEquals(response.status_code, 200)

    def test_should_block_unauthenticated_request(self):
        response = self.client.get("/users")
        self.assertEquals(response.status_code, 401)

    def test_should_fail_to_authenticate_with_invalid_token(self):
        response = self.client.get("/users",  **{'HTTP_AUTHORIZATION':'Token dfdad'})
        self.assertEquals(response.status_code, 401)

    def test_should_list_all_users(self):
        response = self.client.get("/users",  **{'HTTP_AUTHORIZATION':'Token testToken'})
        self.assertEquals(response.status_code, 200)
        self.assertIn("username", response.json()[0])