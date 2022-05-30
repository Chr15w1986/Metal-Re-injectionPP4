""" Posts app configuration file """
from django.apps import AppConfig


class PostsConfig(AppConfig):
    """ posts app config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
