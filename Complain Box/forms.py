from django.forms import ModelForm
from .models import Complain

class CustomerForm(ModelForm):
	class Meta:
		model = Complain
		fields = '__all__'