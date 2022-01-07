from django.shortcuts import render

def index(request):
    return render (request,'index.html')
# def images(request):
#     return render (request,'image.html')
def products(request):
    return render (request,'products.html')
  