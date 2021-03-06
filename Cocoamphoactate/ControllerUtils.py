from django.contrib.auth.models import User


class Utils:
    @staticmethod
    def get_user_from_auth(request):
        try:
            user_id = request.auth.user_id
        except ValueError:
            raise ValueError("Invalid authentication token!")
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise User.DoesNotExist("User for given id does not exists!")
