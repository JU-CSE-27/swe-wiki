from django.db import models

# Create your models here.
class AddProduct(models.Model):
    productCaption=models.CharField(max_length=100)
    productImage=models.ImageField(upload_to="img/%y")
    productPrice=models.CharField(max_length=100)
    def __str__(self):
        return self.productCaption
