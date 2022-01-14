from math import ceil
from multiprocessing import context
from django.shortcuts import render
from django.db.models import Q
from app_viewProduct.models import ProductModel

# Create your views here.
#viewing and sorting function
"""
This is a view product and sorting page
Functions name are product_page,latestProduct_page,toHighProduct_page
"""


#search producct
def searchProduct_page(request):
        
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        query = request.GET['search']
       
        #pics = ProductModel.objects.all()
        pics = ProductModel.objects.filter(m_productCaption__icontains= query).order_by('m_productPrice')
        #pics1 = pics.objects.filter(m_productCaption= query).order_by('id')
        return render(request,'app_products/product-grid-view.html',{"pics":pics})

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


       