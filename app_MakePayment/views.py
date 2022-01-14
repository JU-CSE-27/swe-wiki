from django.shortcuts import render,redirect
from .form import MakePaymentForm
from .models import app_MakePayment

# Create your views here.
def makepayment_page(request):
    '''
    Takes a request and present that requested payment taking page.
    
    '''
    if request.method == "POST":
       form=MakePaymentForm(data=request.POST,files=request.FILES)
       if form.is_valid():
          form.save()
          obj=form.instance
          return render(request,"makepayment.html",{"obj":obj})
    else:
        form=MakePaymentForm()
        return render(request,"makepayment.html",{"form":form})
# def new_page(request):
#     return render(request,"addproducts.html")