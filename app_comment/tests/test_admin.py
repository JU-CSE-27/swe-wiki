import pytest 
from app_comment.models import CommentModel,ReplyModel
from django.contrib.auth.models import User
from mixer.backend.django import mixer 
from django.contrib.admin.sites import AdminSite
pytestmark = pytest.mark.django_db 
from .. import admin

class TestPostAdmin:
    def test_excerpt(self):
        
        site=AdminSite()
        post_admin=admin.PostAdmin(CommentModel,site)
        obj=mixer.blend('app_comment.CommentModel',m_comments='shirt is nice')
        result=post_admin.excerpt(obj)
        assert result == 'shirt', 'Should return first few characters'