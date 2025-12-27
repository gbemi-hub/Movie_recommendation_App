from rest_framework import serializers
from . models import Movie, Comment , Like

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id" ,"title", "description" ,"poster_url","genre"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Comment
        fields = ["id" ,"users", "movie" ,"comment"]

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id" ,"users", "movie"]

