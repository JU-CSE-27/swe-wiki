from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms



"""
This is Form page. Forms name are User-creation form, User-data change form

"""


class CreateUserForm(UserCreationForm):

	"""
	:form name:createUserForm
    :inherit: UserCreationForm
    """
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']



class EditProfileForm(UserChangeForm):

	"""
	:form name:UserDataChangeForm
    :inherit: UserChangeForm
    """
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name']
