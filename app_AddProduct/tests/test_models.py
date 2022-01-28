from django.test import TestCase
from app_AddProduct.models import AddProduct

class TestModels(TestCase):

    def setUp(self):
        self.product1=AddProduct.objects.create(
            productCaption='Product 1',
            productImage='a.jpg',
            productPrice='3000'
        )
        
    def test_AddProduct(self):
        self.assertEquals(self.product1.__str__,'Product 1')
