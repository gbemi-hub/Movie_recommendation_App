from django.urls import path
from .views import (
    MovieListView,
    LikeMovieView,
    UnlikeMovieView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    GenreRecommendationView
)

urlpatterns = [
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movies/genre/<str:genre>/", GenreRecommendationView.as_view(), name="genre-recommendation"),  # recommendations
    path("movies/<int:movie_id>/like/", LikeMovieView.as_view(), name="like-movie"),
    path("movies/<int:movie_id>/unlike/", UnlikeMovieView.as_view(), name="unlike-movie"),
    path("movies/<int:movie_id>/comments/", CommentCreateView.as_view(), name="create-comment"),
    path("comments/<int:comment_id>/", CommentUpdateView.as_view(), name="update-comment"),
    path("comments/<int:comment_id>/delete/", CommentDeleteView.as_view(), name="delete-comment"),
]

