from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SongForm
from .models import Song


class AddSong(CreateView, LoginRequiredMixin):
    form_class = SongForm
    template_name = 'tracks/add-song.html'
    success_url = reverse_lazy('song-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SongList(ListView):
    model = Song
    template_name = 'tracks/song-list.html'
    context_object_name = 'songs'
    queryset = Song.objects.all().order_by('title')
    paginate_by = 3


class SingleSongDetail(DetailView):
    model = Song
    template_name = 'tracks/single-song.html'
    context_object_name = 'song'
