""" Tracks app configuration module """
from django.apps import AppConfig


class TracksConfig(AppConfig):
    """ Tracks config class """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tracks'
