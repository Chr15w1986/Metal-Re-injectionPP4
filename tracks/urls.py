from django.urls import path
from . import views

APP_NAME = 'tracks'
urlpatterns = [
    path('addsong/', views.AddSong.as_view(), name='add-song'),
    path('song-list/', views.SongList.as_view(), name='song-list'),
    path('single-song/<int:pk>/', views.SingleSongDetail.as_view(),
         name='single-song'),
]
