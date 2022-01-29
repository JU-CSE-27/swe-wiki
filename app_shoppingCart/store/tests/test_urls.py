

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import store,cart,checkout,updateItem,processOrder

class TestUrls(SimpleTestCase):

    def test_store_url_is_resolved(self):
        url = reverse('store')
        self.assertEquals(resolve(url).func, store)

    def test_cart_url_is_resolved(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func, cart)

    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)

    def test_updateItem_url_is_resolved(self):
        url = reverse('updateItem')
        self.assertEquals(resolve(url).func, updateItem)

    def test_processOrder_url_is_resolved(self):
        url = reverse('processOrder')
        self.assertEquals(resolve(url).func, processOrder)