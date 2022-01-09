
from django.shortcuts import render, redirect
from django.http import HttpResponse

from shopping_cart.models import ImageShowModel

"""
This is a shopping cart page
Functions name are cart_page, headImg_page
"""

# Create your views here.
def cart_page(request):

    """
    :param name:request
    :param type:URL
    :return:URL
    """
    return render(request,'order-shopping-cart.html')

def headImg_page(request):

    """
    :param name:request
    :param type:URL
    :return:URL,Dictionary
    """
    
    headImg = ImageShowModel.objects.all()
    return render(request,"order-shopping-cart.html",{'images':headImg})