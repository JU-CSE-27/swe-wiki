from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse

def blog(request):

     return render(request, 'blog-fullwidth-page.html')
