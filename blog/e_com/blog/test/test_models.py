from django.test import TestCase
from blog.models import BlogModel
from django.contrib.auth.models import User


class TestAppModels(TestCase):
    def test_model_str(self):
        m_title= BlogModel.objects.create(m_title="Table")
        m_content=BlogModel.objects.create(m_content="Hi Friends and welcome to the first in a series of posts I have planned for 2022! Each week I will be sharing awesome home decor finds from my favorite sources. I am not a designer nor do I care about “brand names”, I just know what looks good! You can expect to see items that I’m currently coveting from big box stores to small shops. This week, I’m starting with Target because it’s just so easy to find great-looking home decor at great prices. I tend to focus on smaller accent pieces, but I did find a few larger furniture items that are just beautiful.")
        m_slug=BlogModel.objects.create(m_slug="Table32")
        m_image=BlogModel.objects.create(m_image="blog/1.jpg")

        self.assertEqual(str(m_title),"Table")
