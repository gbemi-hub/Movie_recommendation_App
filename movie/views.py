from rest_framework import generics, permissions, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Like, Comment
from .serializers import (
    MovieSerializer,
    RecommendationMovieSerializer,
    LikeSerializer,
    CommentSerializer,
    NestedCommentSerializer

)
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class LikeMovieView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        movie_id = self.kwargs["movie_id"]
        movie = Movie.objects.get(id=movie_id)

        if Like.objects.filter(user=self.request.user, movie=movie).exists():
            raise serializers.ValidationError("You already liked this movie")

        serializer.save(user=self.request.user, movie=movie)


class UnlikeMovieView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()

    def get_object(self):
        movie_id = self.kwargs.get("pk")

        try:
            return Like.objects.get(
                user=self.request.user,
                movie_id=movie_id
            )
        except Like.DoesNotExist:
            raise NotFound("You have not liked this movie yet.")

   

    


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        movie_id = self.kwargs["movie_id"]
        movie = Movie.objects.get(id=movie_id)
        serializer.save(user=self.request.user, movie=movie)


class CommentDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()

    def get_object(self):
        comment_id = self.kwargs.get("pk")
        return get_object_or_404(Comment, id=comment_id, user=self.request.user)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Comment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

        

class CommentUpdateView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    lookup_field = "comment_id"  # important!

    def get_object(self):
        return get_object_or_404(
            Comment,
            id=self.kwargs.get("comment_id"),
            user=self.request.user
        )



class GenreRecommendationView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, genre):
        movies_in_genre = Movie.objects.filter(genre=genre)
        movies_sorted = sorted(
            movies_in_genre, key=lambda m: m.like_set.count(), reverse=True
        )
        serializer = RecommendationMovieSerializer(movies_sorted, many=True)
        return Response(serializer.data)
