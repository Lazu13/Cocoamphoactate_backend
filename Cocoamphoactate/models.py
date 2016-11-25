from django.contrib.auth.models import User
from django.db import models


class Friends(models.Model):
    user_one = models.ForeignKey(User, related_name="user_sending_invitation", on_delete=models.CASCADE)
    user_two = models.ForeignKey(User, related_name="user_receiving_invitation", on_delete=models.CASCADE)


class Game(models.Model):
    title = models.CharField(max_length=255)
    score = models.FloatField
    description = models.CharField
    platform = models.CharField(max_length=20)


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_having_fav_game")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="favorite_game")


class GameLib(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class FriendsPending(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_that_send_invitation")
    user_two = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_that_has_to_accept")


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.CharField
