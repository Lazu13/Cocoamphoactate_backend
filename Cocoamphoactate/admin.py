from django.contrib import admin

from Favorites.models import Favorites
from Friends.models import Friends
from FriendsPending.models import FriendsPending
from Game.models import Game
from GameLib.models import GameLib
from Reviews.models import Reviews

admin.site.register(Friends)
admin.site.register(Favorites)
admin.site.register(Game)
admin.site.register(GameLib)
admin.site.register(FriendsPending)
admin.site.register(Reviews)
