from django.db import models
# Create your models here.
class app_MakePayment(models.Model):
     '''
     A class for payment

     Attributes
     ----------
     userName:str
         user name
     userEmail:
         the user's email
     userPhone:
        the user's phone number
     userAddress:str
        the address of the user
     userAmount:int
       the amount user will pay
     '''
     userName=models.CharField(max_length=100)
     userEmail=models.CharField(max_length=100)
     userPhone=models.CharField(max_length=100)
     userAddress=models.CharField(max_length=100)
     userAmount= models.IntegerField()
    


