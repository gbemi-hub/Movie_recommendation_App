from rest_framework import serializers
from .models import Movie, Comment, Like


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "poster_url", "genre"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "users", "movie", "comment"]


class NestedCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # shows username instead of ID

    class Meta:
        model = Comment
        fields = ["id", "user", "comment"]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "users", "movie"]


class RecommendationMovieSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    comments = NestedCommentSerializer(many=True, read_only=True, source="comment_set")

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "poster_url", "genre", "likes_count", "comments"]

    def get_likes_count(self, obj):
        return obj.like_set.count()
