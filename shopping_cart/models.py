from django.db import models

# Create your models here.


# model for header and logo

class UiImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'UiImage/')
    