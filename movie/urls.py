from django.urls import path
from .views import (
    MovieListView,
    LikeMovieView,
    UnlikeMovieView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

urlpatterns = [
    # Movies
    path("movies/", MovieListView.as_view(), name="movie-list"),

    # Likes for movies
    path("movies/<int:movie_id>/like/", LikeMovieView.as_view(), name="like-movie"),
    path("movies/<int:movie_id>/unlike/", UnlikeMovieView.as_view(), name="unlike-movie"),

    # Comments
    path("movies/<int:movie_id>/comments/", CommentCreateView.as_view(), name="create-comment"),
    path("comments/<int:comment_id>/update/", CommentUpdateView.as_view(), name="update-comment"),
    path("comments/<int:comment_id>/delete/", CommentDeleteView.as_view(), name="delete-comment"),
]
