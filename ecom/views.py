from django.shortcuts import render
from django.core.mail import send_mail
from .contact import contactForm


"""
This is a function
--------------

index function

"""


def index(request):
    """
    :param name: request- render index page
    :param type: url
    :return: url
    """
    return render (request,'index.html')

"""
This is a Model
--------------

Contact Model

"""

def contact(request):
    """
    :param name: request- render contact page
    :param type: url
    :return: url
    """
    form = contactForm()
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message_subject = request.POST['message_subject']
        message = request.POST['message']
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
        #send mail
        """send_mail(
            message_name,#subject
            message,#messsage
            message_email, # from email
            ['tazel@gmail.com'], #to email
        )"""
        context = {'form':form}
        
        #return render(request, 'contact.html', context)
        return render(request, 'contact.html',{'message_name':message_name})
        
    else:
        return render(request, 'contact.html')

def home(request):
    """
    :param name: request- render index page
    :param type: url
    :return: url
    """
    return render (request,'home.html')