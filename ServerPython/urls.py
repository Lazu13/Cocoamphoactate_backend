from django.conf.urls import url
from django.contrib import admin

from rest_framework.authtoken import views
from Cocoamphoactate.controllers.UserController import UserController
from Cocoamphoactate.controllers.GameController import GameController
from Cocoamphoactate.controllers.FriendsController import FriendsController
from Cocoamphoactate.controllers.FriendsPendingController import FriendsPendingController
from Cocoamphoactate.controllers.GameLibController import GameLibController
from Cocoamphoactate.controllers.ReviewsController import ReviewsController
from Cocoamphoactate.controllers.FavoritesController import FavoritesController

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^users/login$', UserController.login_user),

    url(r'^users$', UserController.get_users),
    url(r'^users/register$', UserController.register),
    url(r'^user$', UserController.get_put_delete_user),

    url(r'^games$', GameController.get),
    url(r'^games/(?P<pk>[0-9]+)$', GameController.get_put_delete_game),

    url(r'^friends$', FriendsController.get),
    url(r'^friends/(?P<pk>[0-9]+)$', FriendsController.get_put_delete_friends),

    url(r'^friends/pending$', FriendsPendingController.get_all_pending_ivites),
    url(r'^friends/pending/add$', FriendsPendingController.invite_user),
    url(r'^friends/pending/sent', FriendsPendingController.get_sent_by_me),
    url(r'^friends/pending/received', FriendsPendingController.get_received),
    url(r'^friends/pending/accept/(?P<pk>[0-9]+)$', FriendsPendingController.accept_invite),


    url(r'^gamelib$', GameLibController.get),
    url(r'^gamelib/(?P<pk>[0-9]+)$', GameLibController.get_put_delete_lib),

    url(r'^reviews$', ReviewsController.get),
    url(r'^reviews/(?P<pk>[0-9]+)$', ReviewsController.get_put_delete_review),

    url(r'^favs$', FavoritesController.get),
    url(r'^favs/(?P<pk>[0-9]+)$', FavoritesController.get_put_delete_favorite),
]
