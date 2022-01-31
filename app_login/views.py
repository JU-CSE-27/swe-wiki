
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from app_login.forms import EditProfileForm

from django.contrib.auth import authenticate, login, logout,update_session_auth_hash

from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
from .models import *
from .forms import CreateUserForm


"""
There are  home page, registration page, login page,logout page
Function name are home_page,registration_page, login_page,logout_page,userProfile_page,editProfile_page,changePassword_page
"""
def home_page(request):
		"""
		:function name: home_page
		:param name: request
		:param type: URL
		:return:URL
		"""
		return render(request, 'homepage1.html')

def registration_Page(request):
		"""
		:function name: registration_Page
		:param name: request
		:param type: URL
		:return:URL,DICTIONARY
		"""
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

def login_page(request):
	"""
	:function name: login_page
    :param name: request
    :param type: URL
    :return:URL,DICTIONARY
    """
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

def logout_page(request):
	"""
	:function name: logout_page
    :param name: request
    :param type: URL
    :return:URL
    """
	logout(request)
	return HttpResponseRedirect(reverse('app_login:home'))

def userProfile_page(requset):
	"""
	:function name: userProfile_page
    :param name: request
    :param type: URL
    :return:URL,DICTIONARY
    """
	args = {'user':requset.user}
	return render(requset, 'view-user-profile.html',args) 

def editProfile_page(request):
	"""
	:function name: editProfile_page
    :param name: request
    :param type: URL
    :return:URL,DICTIONARY
    """
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance = request.user)

		if form.is_valid():
			form.save()
			#return redirect('profile/')
			return HttpResponseRedirect(reverse('app_login:profile'))
	else:
		form = EditProfileForm(instance = request.user)
		args = {'form':form}
		return render(request,'edit-user-profile.html',args)


def changePassword_page(request):
	"""
	:function name: changePassword_page
    :param name: request
    :param type: URL
    :return:URL,DICTIONARY
    """
	if request.method == 'POST':
		form = PasswordChangeForm(data = request.POST, user = request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			#return redirect('profile/')
			return HttpResponseRedirect(reverse('app_login:profile'))
		
		else:
			return HttpResponseRedirect(reverse('app_login:profile'))

        
	else:
		form = PasswordChangeForm(user = request.user)
		args = {'form':form}
		return render(request,'change-password.html',args)

	    





	   





	







