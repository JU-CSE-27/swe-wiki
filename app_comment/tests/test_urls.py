from django.test import SimpleTestCase
from django.urls import reverse,resolve
from django.urls.base import resolve
from app_comment.views import comment_page


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse("app_comment:comment")
        print(resolve(url))
        self.assertEquals(resolve(url).func,comment_page)