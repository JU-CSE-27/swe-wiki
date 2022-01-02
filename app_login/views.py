
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm


def home(request):

     return render(request, 'app_login/home.html')

def registerPage(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('app_login:login'))
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return HttpResponseRedirect(reverse('app_login:login'))


		context = {'form':form}
		return render(request, 'app_login/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('app_login:home'))
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('app_login:home'))
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'app_login/login_acc.html', context)

def logoutUser(request):
	logout(request)
	return HttpResponseRedirect(reverse('app_login:home'))
