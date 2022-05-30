""" apps config file"""
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """Home app configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
