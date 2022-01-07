from django.shortcuts import render
from .models import ProductModel

# Create your views here.
#viewing and sorting function
def product_page(request):
        pics = ProductModel.objects.all()
        return render(request,'viewProduct.html',{"pics":pics})

def latestProduct_page(request):
        pics = ProductModel.objects.filter().order_by('id')
        return render(request,'latest.html',{"pics":pics})

def toLowProduct_page(request):
        pics = ProductModel.objects.filter().order_by('-m_productPrice')
        return render(request,'latest.html',{"pics":pics})

def toHighProduct_page(request):
        pics = ProductModel.objects.filter().order_by('m_productPrice')
        return render(request,'latest.html',{"pics":pics})

