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
<<<<<<< HEAD
        allProducts = ProductModel.objects.all()
        return render(request,'product-grid-view.html',{"allProducts":allProducts})
=======
        pics = ProductModel.objects.all()
        return render(request,'app_products/product-grid-view.html',{"pics":pics})
>>>>>>> 81a0ce53034d1a5f5003e5222084c40ad0d2f602


def latestProduct_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
<<<<<<< HEAD
        allProducts = ProductModel.objects.filter().order_by('id')
        return render(request,'product-grid-view.html',{"allProducts":allProducts})
=======
        pics = ProductModel.objects.filter().order_by('id')
        return render(request,'app_products/product-grid-view.html',{"pics":pics})
>>>>>>> 81a0ce53034d1a5f5003e5222084c40ad0d2f602

def toLowProduct_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
<<<<<<< HEAD
        allProducts = ProductModel.objects.filter().order_by('-m_productPrice')
        return render(request,'product-grid-view.html',{"allProducts":allProducts})
=======
        pics = ProductModel.objects.filter().order_by('-m_productPrice')
        return render(request,'app_products/product-grid-view.html',{"pics":pics})
>>>>>>> 81a0ce53034d1a5f5003e5222084c40ad0d2f602

def toHighProduct_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
<<<<<<< HEAD
        allProducts = ProductModel.objects.filter().order_by('m_productPrice')
        return render(request,'product-grid-view.html',{"allProducts":allProducts})
=======
        pics = ProductModel.objects.filter().order_by('m_productPrice')
        return render(request,'app_products/product-grid-view.html',{"pics":pics})
>>>>>>> 81a0ce53034d1a5f5003e5222084c40ad0d2f602


       