""" Views for tracks app """

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import SongForm
from .models import Song


class SongList(ListView):
    """ Songlist view for all tracks (Track list)"""
    model = Song
    template_name = 'tracks/song-list.html'
    context_object_name = 'songs'
    queryset = Song.objects.all().order_by('-added_on')
    paginate_by = 3


class UserSongList(ListView):
    """ Usersonglist view for user added tracks (My tracks)"""
    template_name = 'tracks/user-songs.html'
    model = Song
    context_object_name = 'usersongs'
    paginate_by = 3

    def get_queryset(self):
        return Song.objects.filter(
            author=self.request.user, status=1).order_by('-added_on')


class AddSong(CreateView, LoginRequiredMixin):
    """ Addsong form view to allow users to add tracks (Add song)
         while logged in"""
    form_class = SongForm
    template_name = 'tracks/add-song.html'
    success_url = reverse_lazy('song-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SingleSongDetail(DetailView):
    """ Singlesong view to allow users to listen to
         and rate tracks (Rate a Track)"""
    model = Song
    template_name = 'tracks/single-song.html'
    context = {'song': Song}


class DeleteSong(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Deletesong view to allow logged in users to remove their
         own addition from the database"""
    model = Song
    template_name = 'tracks/delete-song.html'
    success_url = reverse_lazy('song-list')

    def test_func(self):
        self.object = self.get_object()
        return self.object.author == self.request.user


class UpdateSong(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Updatesong view to allow logged in users to edit their
     own addition in the database"""
    model = Song
    form_class = SongForm
    template_name = 'tracks/update-song.html'
    success_url = reverse_lazy('song-list')

    def test_func(self):
        self.object = self.get_object()
        return self.object.author == self.request.user
