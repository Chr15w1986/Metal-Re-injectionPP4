from django.urls import path
from . import views

app_name = 'tracks'
urlpatterns = [
    path('addsong/', views.AddSong.as_view(), name='add-song'),
]
