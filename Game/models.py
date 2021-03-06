from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=1000, default="none")
    platform = models.CharField(max_length=20)
    url = models.CharField(max_length=200, default="https://az853139.vo.msecnd.net/static/images/not-found.png")


class Score(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game_being_scored")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_who_scores")
    score = models.FloatField(max_length=10, default=5)


# Create your models here.
