from django.shortcuts import render
from .models import AddProduct

# Create your views here.
def addproduct_page(request):
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
    '''Takes a request and present that requested admin added product showing page.'''
>>>>>>> faf07d4f49f8f244dc3f00cf53f2fca34ec0286b
>>>>>>> bed44d0afa3ec01cd171905be06cae7f5c253dd6
    pics=AddProduct.objects.all()
    return render(request,'addproducts.html',{"pics":pics})
