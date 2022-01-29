

from http import client
from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from store.models import Customer,Product,Order,OrderItem,ShippingAddress
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.store_url = reverse('store')
        self.cart_url = reverse('cart')
        self.checkout_url = reverse('checkout')

    def testCustomer(self):
        response = self.client.get(self.store_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response,'store/main.html')

    def testProduct(self):
        response = self.client.get(self.cart_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response,'store/cart.html')

    def testCheckout(self):
        response = self.client.get(self.checkout_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response,'store/checkout.html')


