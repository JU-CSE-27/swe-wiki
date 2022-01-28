from django.db import models

# Create your models here.
class AddProduct(models.Model):
    '''
    A class to represent a Product


    Attributes
    ----------
    productCaption:str
                  product name
    productImage:img
                 product image
    productPrice:str
                product price in dollar
    '''
    productCaption=models.CharField(max_length=100)
    productImage=models.ImageField(upload_to="img/%y")
    productPrice=models.CharField(max_length=100)
    def __str__(self):
        '''
        A method that return the product caption
        '''
        return self.productCaption
