from django.urls import path
from cinema.views import MovieList, MovieDetail

urlpatterns = [
    path("movies/", MovieList, name="movie-list"),
    path("movies/<int:pk>/", MovieDetail, name="movie-detail"),
]

app_name = "cinema"
