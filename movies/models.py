from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=200)


class Movie(models.Model):
    adult = models.BooleanField()
    genres = models.CharField(max_length=200)
    popularity = models.IntegerField()
    original_language = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    poster_path = models.TextField()
    title = models.CharField(max_length=200)
    vote_average = models.IntegerField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    release_date = models.DateField()
    video = models.CharField(max_length=500)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    # genre_relation = models.ManyToManyField(Genre, related_name = 'movies', blank=True)



class Review(models.Model): 
    star = models.IntegerField()
    content = models.TextField()
    star = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)





# class Score(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     content = models.CharField(max_length=140)
#     score = models.IntegerField()
#     movie = models.ForeignKey(Movie, related_name='scores', on_delete=models.CASCADE)