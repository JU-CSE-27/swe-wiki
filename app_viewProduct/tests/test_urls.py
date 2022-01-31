
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.urls.base import resolve
from app_viewProduct.views import product_page

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('app_viewProduct:viewProduct')
        print(resolve(url))
        self.assertEquals(resolve(url).func,product_page)


