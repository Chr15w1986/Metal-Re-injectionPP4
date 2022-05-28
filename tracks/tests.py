""" Testing module for spotify URLs """

import unittest
from django.test import TestCase
from django.contrib.auth import get_user_model
from .spotify_tools import test_and_rebuild_link
from .models import Song
from .forms import SongForm


class TestSpotifyTools(unittest.TestCase):
    """Tools for testing custom spotify validation tool"""
    def test_invalid_url(self):
        """Tests an incorrect URL"""
        url_to_test = 'www.google.com'
        rebuilt_url = test_and_rebuild_link(url_to_test)
        expected_output = False

        self.assertEqual(rebuilt_url, expected_output)

    def test_valid_url(self):
        """Tests an correct URL"""
        url_to_test = 'https://open.spotify.com/track/421eObjg0DTm2qajJl5OJm?si=fb5b7307c0434ab5'
        rebuilt_url = test_and_rebuild_link(url_to_test)
        expected_output = 'https://open.spotify.com/embed/track/421eObjg0DTm2qajJl5OJm'

        self.assertEqual(rebuilt_url, expected_output)

    def test_valid_domain_wrong_id(self):
        """Tests an invalid song"""
        url_to_test = 'https://open.spotify.com/track/101'
        rebuilt_url = test_and_rebuild_link(url_to_test)
        expected_output = False

        self.assertEqual(rebuilt_url, expected_output)

    def test_invalid_domain_correct_id(self):
        """Tests an valid song with wrong domain"""
        url_to_test = 'https://open.spotty.com/track/421eObjg0DTm2qajJl5OJm?si=fb5b7307c0434ab5'
        rebuilt_url = test_and_rebuild_link(url_to_test)
        expected_output = 'https://open.spotify.com/embed/track/421eObjg0DTm2qajJl5OJm'

        self.assertEqual(rebuilt_url, expected_output)


class TestAddSong(TestCase):
    """ Tests for Form Submission """
    def setUp(self):
        """ Initial setup for all tests, for logging in """
        # Setup Username and Password
        username = "Test_Account"
        pswd = "Test_Password" # noqa
        # Get User model, assign to self, and log in
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username=username,
                                                   password=pswd,
                                                   is_superuser=True)
        logged_in = self.client.login(username=username, password=pswd)
        # Test if login is successful
        self.assertTrue(logged_in)

    def test_valid_form(self):
        """Tests Valid Form Submission"""
        data = {
            'title': "Song",
            'artist': "Artist",
            'original_artist': "Original",
            'url': "https://open.spotify.com/embed/track/421eObjg0DTm2qajJl5OJm"
        }
        # Send HTTP Response to addsong with Data
        response = self.client.post("/tracks/addsong/", data, follow=True)
        # Query how many songs are in the DB
        songs_in_database = len(Song.objects.all())
        # Test 1 song is in Database
        self.assertEqual(songs_in_database, 1)
        # Test Redirected to Songs List after submission
        self.assertRedirects(response, '/tracks/song-list/')

    def test_form_validation_invalid_url(self):
        """Tests Invalid Form Submission (Not a URL)"""
        # Prepare invalid form data (not a valid URL)
        data = {
            'title': "Song",
            'artist': "Artist",
            'original_artist': "Original",
            'url': "donkey"
        }
        form = SongForm(data=data)
        # Ensure url is validated
        self.assertIn("Enter a valid URL.", form.errors['url'])
        # Send HTTP Response to addsong with data
        response = self.client.post("/tracks/addsong/", data, follow=True)
        # Query how many songs are in the DB
        songs_in_database = len(Song.objects.all())
        # Test 0 songs are in Database
        self.assertEqual(songs_in_database, 0)
        # Test the user remains on the add-song page
        self.assertTemplateUsed(response, 'tracks/add-song.html')
