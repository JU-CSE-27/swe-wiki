from django.db import models

# Create your models here.
# Create your models here.
class Sketch(models.Model):
    
     caption=models.CharField(max_length=100)
     sketch=models.ImageField(upload_to="img/%y")
     def __str__(self):
         return self.caption
