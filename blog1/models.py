from django.db import models


from django.contrib.auth.models import User
from froala_editor.fields import FroalaField


class BlogModel(models.Model):
    m_title =models.CharField(max_length=1000)
    m_content =FroalaField()
    m_slug =models.SlugField(max_length=1000)
    m_image = models.ImageField(upload_to='blog')
    m_created_at = models.DateTimeField(auto_now_add=True)
    m_upload_to =models.DateTimeField(auto_now=True)