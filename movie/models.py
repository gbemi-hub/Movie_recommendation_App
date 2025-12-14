from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length = 225)
    description = models.TextField()
    poster_url = models.URLField()
    genre = models.CharField(max_length = 225)


    def __str__(self):
        return self.title


class Like(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE)
    movie =  models.ForeignKey(Movie,on_delete=models.CASCADE)

class Comment(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE)
    movie =  models.ForeignKey(Movie,on_delete=models.CASCADE)
    Comment = models.TextField()