from django.shortcuts import render
from .models import AddProduct

# Create your views here.
def addproduct_page(request):
    '''Takes a request and present that requested admin added product showing page.


    Parameters
    ----------
    :param request:url
          request of a certain page

    Returns
    -------
    :return:url
          Page with updated image

    '''
    pics=AddProduct.objects.all()
    return render(request,'addproducts.html',{"pics":pics})
