from django.shortcuts import render
from app_viewProduct.models import ProductModel

# Create your views here.
#viewing and sorting function
"""
This is a view product and sorting page
Functions name are product_page,latestProduct_page,toHighProduct_page
"""
def product_page(request):
        
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        pics = ProductModel.objects.all()
        return render(request,'app_products/product-grid-view.html',{"pics":pics})


def latestProduct_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        pics = ProductModel.objects.filter().order_by('id')
        return render(request,'app_products/product-grid-view.html',{"pics":pics})

def toLowProduct_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        pics = ProductModel.objects.filter().order_by('-m_productPrice')
        return render(request,'app_products/product-grid-view.html',{"pics":pics})

def toHighProduct_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        pics = ProductModel.objects.filter().order_by('m_productPrice')
        return render(request,'app_products/product-grid-view.html',{"pics":pics})


def regularOffer_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        pics = ProductModel.objects.filter(  m_regularDiscount__gt=0)
        return render(request,'app_products/regularOffer.html',{"pics":pics})

def stuOffer_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        pics = ProductModel.objects.filter( m_studentDiscount__gt=0)
        return render(request,'app_products/stuOffer.html',{"pics":pics})


def eidOffer_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        pics = ProductModel.objects.filter( m_eidDiscount__gt=0)
        return render(request,'app_products/eidOffer.html',{"pics":pics})


       