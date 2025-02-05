from django.urls import path, include
from rest_framework import routers
from cinema.views import (MovieViewSet,
                          GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail,
                          CinemaHallViewSet)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinemahall_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create"})
cinemahall_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "patch": "partial_update",
    "put": "update",
    "delete": "destroy"})

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinemahall/", cinemahall_list, name="cinema-hall-list"),
    path("cinemahall/<int:pk>/", cinemahall_detail, name="cinema-hall-detail"),
]
