from django.conf.urls import url
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app_image.views import product_page

class TestUrls(SimpleTestCase):
    
    def test_list_url_is_resolved(self):
        url = reverse('app_image:productView')
        print(resolve(url))
        self.assertEquals(resolve(url).func,product_page)
