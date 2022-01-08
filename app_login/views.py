
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

"""
There are  home page, registration page, login page,logout page
Function name are home_page,registration_page, login_page,logout_page
"""
from .models import *
from .forms import createUserForm


def home_page(request):
    """
	:function name: home_page
    :param name: request
    :param type: URL
    :return:URL
    """

    return render(request, 'homepage1.html')

def register_page(request):

	"""
	:function name: register_page
    :param name: request
    :param type: URL
    :return:URL
    """
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('app_login:login'))
	else:
		cuserForm = createUserForm()
		if request.method == 'POST':
			cuserForm = createUserForm(request.POST)
			if cuserForm.is_valid():
				cuserForm.save()
				userName = cuserForm.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + userName)

				return HttpResponseRedirect(reverse('app_login:login'))


		context = {'form':cuserForm}
		return render(request, 'app_login/register.html', context)

def login_page(request):
	"""
	:function name: login_page
    :param name: request
    :param type: URL
    :return:URL
    """
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('app_login:home'))
	else:
		if request.method == 'POST':
			userName = request.POST.get('username')
			userPassword =request.POST.get('password')

			userAuth = authenticate(request, username=userName, password=userPassword)

			if userAuth is not None:
				login(request, userAuth)
				return HttpResponseRedirect(reverse('app_login:home'))
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'app_login/login_acc.html', context)

def logout_page(request):
	"""
	:function name: logout_page
    :param name: request
    :param type: URL
    :return:URL
    """
	logout(request)
	return HttpResponseRedirect(reverse('app_login:home'))
