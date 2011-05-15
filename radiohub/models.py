from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    name = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    path = models.FilePathField(max_length=200)

class Playlist(models.Model):
    name = models.CharField(max_length=200)
    criteria = models.CharField(max_length=200)
    consume = models.BooleanField()
    private = models.BooleanField()

class Vote(models.Model):
    playlist = models.ForeignKey(Playlist)
    song = models.ForeignKey(Song)
    vote = models.SmallIntegerField()

