import unittest
from django.test import TestCase
from app_image.models import ProductModel
from django.contrib.auth.models import User

class TestAppModels(TestCase):
    def test_model_str(self):
        m_productCaption=ProductModel.objects.create(m_productCaption="Table")
        m_productImage=ProductModel.objects.create(m_productImage="img/22/img04.png")
        m_productPrice=ProductModel.objects.create(m_productPrice=230.8)
        m_productQuantity=ProductModel.objects.create(m_productQuantity=4)

        self.assertEqual(str(m_productCaption),"Table")
