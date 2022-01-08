from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
"""
There is a form name createForm

"""
class createUserForm(UserCreationForm):
	"""
	:form name:createUserForm
    :inherit: UserCreationForm
    """
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
