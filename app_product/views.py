from django.shortcuts import render
from .models import Image

# Create your views here.
def product_page(request):
   return render(request, 'products.html')
def image_page(request):
   pics=Image.objects.all()
   return render(request, 'image.html')
    