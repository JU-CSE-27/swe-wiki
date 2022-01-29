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
    m_name = models.CharField(max_length=255)
    m_email = models.EmailField(unique=True)
    m_subject = models.CharField(max_length=255)
    m_message = models.CharField(max_length=255)
    def __str__(self):
        return self.m_name + ' ' + self.m_email + ' ' +self.m_subject+ ' ' + self.m_message


class Post(models.Model):
    body = models.TextField()
    