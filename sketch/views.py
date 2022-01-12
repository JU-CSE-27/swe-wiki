from django.shortcuts import render,redirect
from .form import SketchForm
from .models import Sketch

# Create your views here.
def sketch_page(request):
    '''Takes a request and present that requested seller or anyone added product showing page.'''
    if request.method == "POST":
       form=SketchForm(data=request.POST,files=request.FILES)
       if form.is_valid():
          form.save()
          obj=form.instance
          return render(request,"sketch.html",{"obj":obj})
    else:
        form=SketchForm()
        img=Sketch.objects.all()
        return render(request,"sketch.html",{"img":img,"form":form})
