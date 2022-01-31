import pytest
from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer

from app_blog import models
from  app_blog import admin



pytestmark = pytest.mark.django_db


class TestBlogAdmin:
    def test_excerpt(self):
        site = AdminSite()
        post_admin = admin.ModelBlogAdmin(models.ModelBlog,site)

        obj = mixer.blend('app_blog.ModelBlog', body = 'Hello World')