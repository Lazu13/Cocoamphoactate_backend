from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Friends)
admin.site.register(Favorites)
admin.site.register(Game)
admin.site.register(GameLib)
admin.site.register(FriendsPending)
admin.site.register(Reviews)
