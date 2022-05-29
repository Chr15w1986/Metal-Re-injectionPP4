""" Spotify url rebuild module """
from urllib.parse import urlparse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

os.environ["SPOTIPY_CLIENT_ID"] = "ee3d2bde9e494a87990ee51eeaa640eb"

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


def test_and_rebuild_link(url_to_test):

    try:
        track = sp.track(url_to_test)
        original_track_url = track['external_urls']['spotify']
        parsed_url = urlparse(original_track_url)
        path = parsed_url.path
        rebuilt_url = parsed_url._replace(path='embed'+path).geturl()
        return rebuilt_url

    except spotipy.exceptions.SpotifyException:
        return False
