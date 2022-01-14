from django.forms import ModelForm
from .models import Contact

class contactForm(ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'