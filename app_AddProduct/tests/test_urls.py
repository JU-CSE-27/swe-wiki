from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ecom.views import index,products
from app_AddProduct.views import addproduct_page
from sketch.views import sketch_page


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        assert 1 == 2
    #     url=reverse('index')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func,index)
    # def test_product_url_is_resolved(self):
    #     url=reverse('products')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func,products)
    # def test_addproduct_url_is_resolved(self):
    #     url=reverse('addproduct')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func,addproduct_page)
    # def test_sketch_url_is_resolved(self):
    #     url=reverse('home')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func,sketch_page)
