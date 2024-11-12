from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_apps_page_status_code(self):
        response = self.client.get('/apps/')
        self.assertEqual(response.status_code, 200)

    def test_modules_page_status_code(self):
        response = self.client.get('/modules/')
        self.assertEqual(response.status_code, 200)

    def test_links_page_status_code(self):
        response = self.client.get('/links/')
        self.assertEqual(response.status_code, 200)

    def test_guides_page_status_code(self):
        response = self.client.get('/guides/')
        self.assertEqual(response.status_code, 200)
