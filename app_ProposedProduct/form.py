from django import forms
from .models import ProposedProduct

class ProposedProductForm(forms.ModelForm):
    '''
    A class to represent a Form
    
    '''


    class Meta:
           model=ProposedProduct
           fields=("productCaption","productPrice","productImage")