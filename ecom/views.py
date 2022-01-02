from django.shortcuts import render

def index(request):
    return render (request,'index.html')
def products(request):
    return render (request,'products.html')
  