from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *
"""
: model name: BlogModel
:inherit: models.Model

"""

class BlogModel(models.Model):
    m_title = models.CharField(max_length=1000)
    m_content = FroalaField()
    m_slug = models.SlugField(max_length=1000, null=True , blank=True)
    m_image = models.ImageField(upload_to='blog')
    m_createdAt = models.DateTimeField(auto_now_add=True)
    m_uploadTo = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.m_title

    def save(self , *args, **kwargs):
        self.m_slug = generate_slug(self.m_title)
        super(BlogModel, self).save(*args, **kwargs)
