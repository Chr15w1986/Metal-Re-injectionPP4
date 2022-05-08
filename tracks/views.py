from django.shortcuts import render, reverse
from django.views.generic import CreateView
from .forms import SongForm
from django.contrib.auth.mixins import LoginRequiredMixin

class AddSong(CreateView, LoginRequiredMixin):
    form_class = SongForm
    template_name = 'tracks/add-song.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
