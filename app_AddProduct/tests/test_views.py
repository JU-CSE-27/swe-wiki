

from django.test import TestCase, client
from django.test import TestCase, Client
from django.urls import reverse
from app_AddProduct.models import AddProduct


class TestViews(TestCase):

    def setUp(self):
        self.client=Client()
        self.addedproduct_url=reverse('addproduct')
        

    def test_products_GET(self):
        client=Client()
        response=client.get(reverse('addproduct'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'addproducts.html')

