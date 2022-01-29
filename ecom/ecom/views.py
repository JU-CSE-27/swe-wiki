from re import template
from django.shortcuts import render
from django.core.mail import send_mail
from .contact import contactForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
    

class HomeView(TemplateView):
    """
    :param name: TemplateView- render Testing
    :param type: url
    :return: none
    """
    template_name = 'ecom/home.html'


class AdminView(TemplateView):
    """
    :param name: TemplateView- render Testing
    :param type: url
    :return: none
    """
    template_name='ecom/home.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)