from django.shortcuts import render
from rest_framework import generics , permissions ,serializers
from . serializers import LikeSerializer, MovieSerializer



class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class LikeMovieView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        movie_id = self.kwargs["movie_id"]
        movie = Movie.objects.get(id=movie_id)

        if Like.objects.filter(user=self.request.user, movie=movie).exists():
            raise serializers.ValidationError("You already liked this movie")

        serializer.save(user=self.request.user, movie=movie)

class UnlikeMovieView(generics.DestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        movie_id = self.kwargs["movie_id"]
        return Like.objects.get(user=self.request.user, movie_id=movie_id)



class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        movie_id = self.kwargs["movie_id"]
        movie = Movie.objects.get(id=movie_id)
        serializer.save(user=self.request.user, movie=movie)

class CommentDeleteView(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        comment_id = self.kwargs["comment_id"]
        return Comment.objects.get(user=self.request.user, id=comment_id)

class CommentUpdateView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        comment_id = self.kwargs["comment_id"]
        return Comment.objects.get(user=self.request.user, id=comment_id)

