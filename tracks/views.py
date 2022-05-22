from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SongForm
from .models import Song


class SongList(ListView):
    model = Song
    template_name = 'tracks/song-list.html'
    context_object_name = 'songs'
    queryset = Song.objects.all().order_by('-added_on')
    paginate_by = 3


class UserSongList(ListView):
    template_name = 'tracks/user-songs.html'
    model = Song
    context_object_name = 'usersongs'
    paginate_by = 3

    def get_queryset(self):
        return Song.objects.filter(
            author=self.request.user, status=1).order_by('-added_on')


class AddSong(CreateView, LoginRequiredMixin):
    form_class = SongForm
    template_name = 'tracks/add-song.html'
    success_url = reverse_lazy('song-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SingleSongDetail(DetailView):
    model = Song
    template_name = 'tracks/single-song.html'
    context = {'song': Song}


class DeleteSong(DeleteView):
    model = Song
    template_name = 'tracks/delete-song.html'
    success_url = reverse_lazy('song-list')


class UpdateSong(UpdateView):
    model = Song
    form_class = SongForm
    template_name = 'tracks/update-song.html'
    success_url = reverse_lazy('song-list')
