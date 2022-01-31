
from unittest import result
import pytest 
from mixer.backend.django import mixer 
from django.contrib.admin.sites import AdminSite
pytestmark = pytest.mark.django_db 


from .. import admin
from .. import models

class TestPostAdmin:
    def text_excerpt(self):
        site = AdminSite()
        post_admin = admin.PostAdmin(models.ProductModel,site)

        obj = mixer.blend('app_viewProduct.ProductModel',m_productCaption="Table Product")
        result = post_admin.get_excerpt(5)
        assert result == 'Table', 'should return first few charecters'
