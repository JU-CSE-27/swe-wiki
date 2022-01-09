from django.db import models

# Create your models here.


# model for header and logo

class UiImageModel(models.Model):
    """
    :model name: UiImageModel
    :inherit: models.Model
    """
    m_UiImageName = models.CharField(max_length=100)
    m_UiImageFile = models.ImageField(upload_to = 'UiImage/')
    