import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestPost:
    def test_model(self):
        obj = mixer.blend('ecom.Post')
        assert obj.pk == 1, 'Should create a Post instance'
