from django.test import TestCase


class TestLandingPageViews(TestCase):

    def test_landing_page_status_code_is_ok(self):
        home_page = self.client.get('/')
        self.assertEqual(home_page.status_code, 200)

    def test_landing_page_status_code_is_not_ok(self):
        home_page = self.client.get('/')
        self.assertNotEqual(home_page.status_code, 403)
