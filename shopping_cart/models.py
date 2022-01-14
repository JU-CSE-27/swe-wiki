from django.db import models

# Create your models here.


# model for header and logo

class ImageShowModel(models.Model):
    
    """
    :model name: ProductModel
    :inherit: models.Model
    """

    m_imageShowName = models.CharField(max_length=100)
    m_imageShowimage = models.ImageField(upload_to = 'UiImage/')
    