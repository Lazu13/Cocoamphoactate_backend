from django.conf.urls import url
from django.contrib import admin

from rest_framework.authtoken import views
from Users.views import UserController
from Game.views import GameController
from GameLib.views import GameLibController
from Friends.views import FriendsController
from FriendsPending.views import FriendsPendingController
from Favorites.views import FavoritesController
from Reviews.views import ReviewsController
from Recommendation.views import RecommendationController
from Search.views import Search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^users/login$', UserController.login_user),

    url(r'^users$', UserController.get_users),
    url(r'^users/register$', UserController.register),
    url(r'^user$', UserController.get_put_delete_user),
    url(r'^users/(?P<pk>[0-9]+)$', UserController.get_user),

    url(r'^games$', GameController.get),
    url(r'^games/add', GameController.post),
    url(r'^games/(?P<pk>[0-9]+)$', GameController.get_put_delete_game),
    url(r'^games/(?P<pk>[0-9]+)/grade$', GameController.add_grade),

    url(r'^friends$', FriendsController.get),
    url(r'^friends/my', FriendsController.get_my_friends),

    url(r'^friends/pending$', FriendsPendingController.get_all_pending_ivites),
    url(r'^friends/pending/add$', FriendsPendingController.invite_user),
    url(r'^friends/pending/sent', FriendsPendingController.get_sent_by_me),
    url(r'^friends/pending/received', FriendsPendingController.get_received),
    url(r'^friends/pending/accept/(?P<pk>[0-9]+)$', FriendsPendingController.accept_invite),

    url(r'^gamelib$', GameLibController.get),
    url(r'^gamelib/(?P<pk>[0-9]+)$', GameLibController.get_put_delete_lib),

    url(r'^reviews/add$', ReviewsController.post_game_review),
    url(r'^reviews/(?P<pk>[0-9]+)$', ReviewsController.get_game_reviews),
    url(r'^reviews/remove/(?P<pk>[0-9]+)$', ReviewsController.remove_review),

    url(r'^favs$', FavoritesController.get),
    url(r'^favs/(?P<pk>[0-9]+)$', FavoritesController.remove_favorite),

    url(r'^users/recommend/type/(?P<t>[0-2])$', RecommendationController.get),
    url(r'^users/recommend/mostPopular$', RecommendationController.get_most_popular),

    url(r'^users/games/search$', Search.search_games),
    url(r'^users/users/search$', Search.search_users),
]
