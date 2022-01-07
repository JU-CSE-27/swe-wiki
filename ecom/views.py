from django.shortcuts import render

def index(request):
    '''Takes a request and present that requested home page.'''
    return render (request,'index.html')
# def images(request):
#     return render (request,'image.html')
def products(request):
    '''Takes a request and present that requested product showing page.'''
    return render (request,'products.html')
def pictures(request):
    '''Takes a request and present that requested page to show uploaded picture from normal html file.'''
    return render (request,'pictures.html')
def uploadimage(request):
    '''Takes a request and present that requested page to upload and show pictures.'''
    return render (request,'uploadimage.html')
  