from django.contrib.auth.models import User
from django.db import models

from Game.models import Game


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.CharField(max_length=1000, default='none')

# Create your models here.
