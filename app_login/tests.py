from django.http import response
from django.test import TestCase
# Create your tests here.
class URLTests(TestCase):
    def test_contactpage(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
