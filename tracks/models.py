""" Models for song-list """
from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class Song(models.Model):
    """ Creates song form """
    title = models.CharField(max_length=25, null=False, blank=False)
    artist = models.CharField(max_length=25, null=False, blank=False)
    original_artist = models.CharField(max_length=25, null=False, blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False,
        related_name='author')
    url = models.URLField(null=False, blank=False)
    added_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['added_on']

    def __str__(self):
        return str(self.title)
