from django.shortcuts import render
from app_viewProduct.models import ProductModel

# Create your views here.
#viewing and sorting function
"""
This is a view product and sorting page
Functions name are product_page,latestProduct_page,toHighProduct_page
"""
def home_page(request):

     return render(request, 'homepage1.html')
     
def product_page(request):
        
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        allProducts = ProductModel.objects.all()
        return render(request,'product-grid-view.html',{"allProducts":allProducts})


def latestProduct_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        allProducts = ProductModel.objects.filter().order_by('id')
        return render(request,'product-grid-view.html',{"allProducts":allProducts})

def toLowProduct_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        allProducts = ProductModel.objects.filter().order_by('-m_productPrice')
        return render(request,'product-grid-view.html',{"allProducts":allProducts})

def toHighProduct_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        allProducts = ProductModel.objects.filter().order_by('m_productPrice')
        return render(request,'product-grid-view.html',{"allProducts":allProducts})


       