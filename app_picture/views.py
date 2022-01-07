from django.shortcuts import render
from .models import Picture

# Create your views here.
def picture_page(request):
    '''Take to the requested picture page to show uploaded pictures.'''
    return render(request, 'pictures.html')
