from django.shortcuts import render , redirect

from blog.models import BlogModel


# Create your views here.

def blog (request):
    blog = BlogModel.objects.all()
    context = {'blog' : blog}
    return render(request, 'home.html',context)


def blog_detail(request , m_slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(m_slug=m_slug).first()
        context['blog_obj']=blog_obj
    except Exception as e:
        print(e)    
    return render(request , 'blog_detail.html',context)