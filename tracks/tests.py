""" Testing module for spotify URLs """

import unittest
from .spotify_tools import test_and_rebuild_link


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
