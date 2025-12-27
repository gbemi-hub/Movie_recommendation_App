from rest_framework import generics, permissions, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Like, Comment
from .serializers import (
    NormalMovieSerializer,
    RecommendationMovieSerializer,
    LikeSerializer,
    CommentSerializer
)

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = NormalMovieSerializer


class LikeMovieView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        movie_id = self.kwargs["movie_id"]
        movie = Movie.objects.get(id=movie_id)

        if Like.objects.filter(users=self.request.user, movie=movie).exists():
            raise serializers.ValidationError("You already liked this movie")

        serializer.save(users=self.request.user, movie=movie)


class UnlikeMovieView(generics.DestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        movie_id = self.kwargs["movie_id"]
        return Like.objects.get(users=self.request.user, movie_id=movie_id)


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        movie_id = self.kwargs["movie_id"]
        movie = Movie.objects.get(id=movie_id)
        serializer.save(users=self.request.user, movie=movie)


class CommentDeleteView(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        comment_id = self.kwargs["comment_id"]
        return Comment.objects.get(users=self.request.user, id=comment_id)


class CommentUpdateView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        comment_id = self.kwargs["comment_id"]
        return Comment.objects.get(users=self.request.user, id=comment_id)


class GenreRecommendationView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, genre):
        movies_in_genre = Movie.objects.filter(genre=genre)
        movies_sorted = sorted(
            movies_in_genre, key=lambda m: m.like_set.count(), reverse=True
        )
        serializer = RecommendationMovieSerializer(movies_sorted, many=True)
        return Response(serializer.data)
