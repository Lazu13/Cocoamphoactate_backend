from django.contrib.auth.models import User
from django.db import models

from Game.models import Game


class GameLib(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)



# Create your models here.
