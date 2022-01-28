from django import forms
from .models import app_MakePayment

class MakePaymentForm(forms.ModelForm):
      
     class Meta:
           model=app_MakePayment
           fields=("userName","userEmail","userPhone","userAddress","userAmount")