from django.contrib.auth.models import User
from rest_framework.decorators import api_view

from Cocoamphoactate.dataloader.dataloader import DataLoader


class Utils:
    @staticmethod
    def get_user_from_auth(request):
        try:
            user_id = request.auth.user_id
            print(user_id)
        except ValueError:
            return ValueError("Invalid authentication token!")
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return User.DoesNotExist("User for given id does not exists!")