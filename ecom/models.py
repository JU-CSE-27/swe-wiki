from django.db import models


    
"""
This is a Contact Model
-----------------------
'A Contact Table'
""" 
# Create your models here.
class Contact(models.Model):
    """
    :param name: model- a contact table created
    :param type: model
    :return: none
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    