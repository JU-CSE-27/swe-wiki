from django.shortcuts import render

def index(request):
    '''Takes a request and present that requested home page.'''
    return render (request,'index.html')
# def images(request):
#     return render (request,'image.html')
def products(request):
    '''Takes a request and present that requested product showing page.'''
    return render (request,'products.html')
  