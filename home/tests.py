""" Home app testing module """
from django.test import TestCase


class TestLandingPageViews(TestCase):
    """ Home page views tests """
    def test_landing_page_status_code_is_ok(self):
        """ test if home page loads correctly """
        home_page = self.client.get('/')
        self.assertEqual(home_page.status_code, 200)

    def test_landing_page_status_code_is_not_ok(self):
        """ test if home page does not load correctly,
            redirect to 403 forbidden """
        home_page = self.client.get('/')
        self.assertNotEqual(home_page.status_code, 403)
