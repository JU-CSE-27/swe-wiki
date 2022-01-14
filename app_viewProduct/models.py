from django.db import models

# Create your models here.
class ProductModel(models.Model):
    """
    :model name: ProductModel
    :inherit: models.Model
    """
    m_productCaption=models.CharField(max_length=50)
    m_productImage=models.ImageField(upload_to="img/%y")
    m_productPrice=models.FloatField(null=True)
    m_productQuantity=models.IntegerField(null=True)
    def __str__(self):
        return self.m_productCaption
