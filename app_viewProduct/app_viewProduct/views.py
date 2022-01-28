from django.shortcuts import render
from app_viewProduct.models import ProductModel

# Create your views here.
#viewing and sorting function
"""
This is a view product, Search Product and sorting product  page
Functions name are product_page,searchProduct_page, latestProduct_page,toHighProduct_page
"""
#search product
def searchProduct_page(request):
        
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        query = request.GET['search']
       
        #pics = ProductModel.objects.all()
        pics = ProductModel.objects.filter(m_productCaption__icontains= query).order_by('m_productPrice')
        return render(request, 'search_products/product-grid-view.html',{"pics":pics})


#search product
def searchProduct_page(request):
        
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        query = request.GET['search']
       
        #pics = ProductModel.objects.all()
        pics = ProductModel.objects.filter(m_productCaption__icontains= query).order_by('m_productPrice')
        return render(request,'app_products/product-grid-view.html',{"pics":pics})




def product_page(request):
        
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        allProducts = ProductModel.objects.all()
        return render(request,'app_products/product-grid-view.html',{"pics": allProducts})


def latestProduct_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        allProducts = ProductModel.objects.filter().order_by('id')
        return render(request,'app_products/product-grid-view.html',{"pics": allProducts})

def toLowProduct_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        allProducts= ProductModel.objects.filter().order_by('-m_productPrice')
        return render(request,'app_products/product-grid-view.html',{"pics": allProducts})

def toHighProduct_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        allProducts = ProductModel.objects.filter().order_by('m_productPrice')
        return render(request,'app_products/product-grid-view.html',{"pics": allProducts})


def regularOffer_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        allProducts = ProductModel.objects.filter(  m_regularDiscount__gt=0)
        return render(request,'app_products/regularOffer.html',{"pics": allProducts})

def stuOffer_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        allProducts = ProductModel.objects.filter( m_studentDiscount__gt=0)
        return render(request,'app_products/stuOffer.html',{"pics": allProducts})


def eidOffer_page(request):
        """
        :param name:request
        :param type:URL
        :return:URL,Dictionary
        """
        allProducts = ProductModel.objects.filter( m_eidDiscount__gt=0)
        return render(request,'app_products/eidOffer.html',{"pics": allProducts})


       
