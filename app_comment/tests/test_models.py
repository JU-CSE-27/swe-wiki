import pytest 
from app_comment.models import CommentModel,ReplyModel
from django.contrib.auth.models import User
from mixer.backend.django import mixer 
pytestmark = pytest.mark.django_db 
class TestPost: 
    def test_model(self): 
        obj = mixer.blend('app_comment.CommentModel') 
        assert obj.pk == 1, 'Should create a Post instance'
    def test_get_excerpt(self):
        obj = mixer.blend('app_comment.CommentModel', m_comments="shirt is nice")
        result = obj.get_excerpt(5)
        assert result == 'shirt', 'Should return first few charecters'

    def test_get_excerpts(self):
        obj = mixer.blend('app_comment.ReplyModel', m_comments="shirt is nice")
        result = obj.get_excerpts(5)
        assert result == 'shirt', 'Should return first few charecters'
