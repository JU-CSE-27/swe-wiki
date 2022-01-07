from django.db import models


from ecom.views import pictures


# Create your models here.
class Picture(models.Model):
    caption=models.CharField(max_length=50)
    pictures=models.ImageField(upload_to="img/%y")
    def __str__(self):
        '''Making caption for uploaded image.'''
        return self.caption
