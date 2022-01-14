from django.http import response
from django.test import TestCase
# Create your tests here.
"""
This is a test
--------------

Url Test

"""
class URLTests(TestCase):
    """
    :param name: Test Case- get a test case
    :param type: TestCase
    :return: none
    """
    def test_contactpage(self):
        """
        :param name: self object- get an object
        :param type: self
        :return: none
        """
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
