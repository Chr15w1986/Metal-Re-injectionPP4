""" Tracks app url module """
from django.urls import path
from . import views

APP_NAME = 'tracks'
urlpatterns = [
    path('addsong/', views.AddSong.as_view(), name='add-song'),
    path('song-list/', views.SongList.as_view(), name='song-list'),
    path('single-song/<int:pk>/', views.SingleSongDetail.as_view(),
         name='single-song'),
    path('single-song/delete-song/<int:pk>', views.DeleteSong.as_view(),
         name='delete-song'),
    path('single-song/update-song/<int:pk>', views.UpdateSong.as_view(),
         name='update-song'),
    path('user-songs/', views.UserSongList.as_view(),
         name='user-songs')
]
