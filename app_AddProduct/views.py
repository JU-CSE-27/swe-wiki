from django.shortcuts import render
from .models import AddProduct

# Create your views here.
def addproduct_page(request):
    '''Takes a request and present that requested admin added product showing page.'''
    pics=AddProduct.objects.all()
    return render(request,'addproducts.html',{"pics":pics})
