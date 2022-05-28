""" Forms module """

from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Song
from .spotify_tools import test_and_rebuild_link


class SongForm(ModelForm):
    """ Creates a form for the user to add a new song to the database,
        including user input url validation"""
    class Meta:
        """ defines how the SongForm class behaves """
        model = Song
        fields = [
            'title',
            'artist',
            'original_artist',
            'url'
        ]

    def clean_url(self):
        """ Cleans and rebuilds user url input within the form,
            including validation for incorrect input """
        url = self.cleaned_data['url']
        rebuilt_url = test_and_rebuild_link(url)
        if not rebuilt_url:
            raise ValidationError("Sorry, that's not a valid Spotify link!")
        return rebuilt_url
