from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


# Create your models here.


class Playlist(models.Model):
    nomi = models.CharField(max_length=150)
    image = models.ImageField(upload_to = 'rasmlar/playlist_rasm')
    about = RichTextField()
    count = models.FloatField()

    def __str__(self):
        return self.nomi


class VideoDars(models.Model):
    nomi = models.CharField(max_length=150)
    izoh = RichTextField()
    video = models.FileField(upload_to='video_darslar/video')
    playlisti = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomi