from django.contrib.auth.models import User
from django.db import models


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_having_fav_game")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="favorite_game")