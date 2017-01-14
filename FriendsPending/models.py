from django.contrib.auth.models import User
from django.db import models

class FriendsPending(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_that_send_invitation")
    user_two = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_that_has_to_accept")


# Create your models here.
