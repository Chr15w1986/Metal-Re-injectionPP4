""" Tracks app admin module """
from django.contrib import admin
from .models import Song


admin.site.register(Song)
