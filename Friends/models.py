from django.contrib.auth.models import User
from django.db import models

class Friends(models.Model):
    user_one = models.ForeignKey(User, related_name="user_sending_invitation", on_delete=models.CASCADE)
    user_two = models.ForeignKey(User, related_name="user_receiving_invitation", on_delete=models.CASCADE)


# Create your models here.
