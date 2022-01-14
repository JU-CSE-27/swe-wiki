
from django.conf.urls import url
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import blog_page , add_blog_page , blog_detail_page


class TestUrls(SimpleTestCase):

    def test_blog_page_url_is_resolved(self):
        url = reverse('blog')
        print(resolve(url))
        self.assertEquals(resolve(url).func,blog_page)

    def test_add_blog_url_is_resolved(self):
        url = reverse('add_blog')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_blog_page)

    def test_blog_detail_url_is_resolved(self):
        url = reverse('blog_detail' , args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, blog_detail_page)
