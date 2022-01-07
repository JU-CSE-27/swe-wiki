
from django.shortcuts import render, redirect
from django.http import HttpResponse

from shopping_cart.models import UiImage

# Create your views here.
def cart(request):
    return render(request,'order-shopping-cart.html')

def head(request):
    headImg = UiImage.objects.all()
    return render(request,"order-shopping-cart.html",{'images':headImg})