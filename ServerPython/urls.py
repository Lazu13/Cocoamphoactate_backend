from django.conf.urls import url
from django.contrib import admin
from Cocoamphoactate import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users$', views.UserApi.get),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserApi.get_put_delete_user),
    url(r'^games$', views.GameApi.get),
    url(r'^games/(?P<pk>[0-9]+)$', views.GameApi.get_put_delete_game),
    url(r'^friends$', views.FriendsApi.get),
    url(r'^friends/(?P<pk>[0-9]+)$', views.FriendsApi.get_put_delete_friends),
]
