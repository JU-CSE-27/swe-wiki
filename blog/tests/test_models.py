import re
from unittest import result
import py
import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestPost:
    def test_model(self):
        obj = mixer.blend ('app_blog.ModelBlog')
        assert obj.pk == 1, 'Should create a blog instance'
    def test_get_excerpt(self):
        obj = mixer.blend("app_blog.ModelBlog" , body = 'Hello World!')
        result = obj.get_excerpt(5)
        expected = 'Hello'
        assert result == expected, ('Should return the given number of character')