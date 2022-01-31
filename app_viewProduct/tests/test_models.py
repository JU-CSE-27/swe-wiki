import pytest 
from mixer.backend.django import mixer 
from app_viewProduct.models import ProductModel
pytestmark = pytest.mark.django_db 
class TestPost: 
    def test_model(self): 
        obj = mixer.blend('app_viewProduct.ProductModel') 
        assert obj.pk == 1, 'Should create a product instance'
    
    def test_get_excerpt(self):
        obj = mixer.blend('app_viewProduct.ProductModel', m_productCaption="Table Product")
        result = obj.get_excerpt(5)
        assert result == 'Table', 'Should return first few charecters'

        #m_productCaption = ProductModel.objects.create(m_productCaption="Table")
        #m_productImage=ProductModel.objects.create(m_productImage="img/22/img04.png")
        #m_productPrice=ProductModel.objects.create(m_productPrice=230)
        #m_productQuantity=ProductModel.objects.create(m_productQuantity=4)

        #self.assertEqual(str(m_productCaption),"Table")
