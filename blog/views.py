from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from blog.models import BlogModel
from blog.form import blogForm


"""
This is a blog page
Funtions name are blog , blog_detail and add_blog

"""

def blog_page (request):

    """
    :param name: request
    :param type: url
    : return: url, Dictionary

    """
    blog = BlogModel.objects.all()
    context = {'blog' : blog}
    return render(request, 'app_blog/home.html',context)


def blog_detail_page (request , m_slug):

    """
    :param name: request , m_slug
    :param type: url, slug
    : return: url, Dictionary


    """
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(m_slug=m_slug).first()
        context['blog_obj']=blog_obj
    except Exception as e:
        print(e)    
    return render(request , 'app_blog/blog_detail.html',context)

def add_blog_page (request):
    """
    :param name: request
    :param type:url
    : return: url, Dictionary

    """
    context = {'form' : blogForm} 
    try:
        if request.method == 'POST':
            form = blogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(
                 m_title = title, 
                m_content = content, m_image = image
            )
            print(blog_obj)
            return redirect('/add-blog/')
            



    except Exception as e :
        print(e)       
    return render(request , 'app_blog/add_blog.html' , context)    



