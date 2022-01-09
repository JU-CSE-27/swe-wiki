from django.shortcuts import render
from .models import AddProduct

# Create your views here.
def addproduct_page(request):
    pics=AddProduct.objects.all()
    return render(request,'addproducts.html',{"pics":pics})
