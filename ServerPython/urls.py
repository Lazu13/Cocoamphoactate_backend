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
from Cocoamphoactate.controllers.RecommendationController import RecommendationController

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^users/login$', UserController.loginUser),

    url(r'^users$', UserController.get_users),
    url(r'^users/register$', UserController.register),
    url(r'^user/$', UserController.get_put_delete_user),

    url(r'^games$', GameController.get),
    url(r'^games/(?P<pk>[0-9]+)$', GameController.get_put_delete_game),
    url(r'^games/(?P<pk>[0-9]+)/grade$', GameController.add_grade),

    url(r'^friends$', FriendsController.get),
    url(r'^friends/(?P<pk>[0-9]+)$', FriendsController.get_put_delete_friends),

    url(r'^friends/pending$', FriendsPendingController.get),
    url(r'^friends/pending/(?P<pk>[0-9]+)$', FriendsPendingController.get_put_delete_firends_pending),

    url(r'^gamelib$', GameLibController.get),
    url(r'^gamelib/(?P<pk>[0-9]+)$', GameLibController.get_put_delete_lib),

    url(r'^reviews$', ReviewsController.get),
    url(r'^reviews/(?P<pk>[0-9]+)$', ReviewsController.get_put_delete_review),

    url(r'^favs$', FavoritesController.get),
    url(r'^favs/(?P<pk>[0-9]+)$', FavoritesController.get_put_delete_favorite),

    url(r'^users/recommend/(?P<pk>[0-9]+)/type/(?P<t>[0-1])$', RecommendationController.get),
    url(r'^users/recommend/mostPopular$', RecommendationController.get_most_popular),
]
