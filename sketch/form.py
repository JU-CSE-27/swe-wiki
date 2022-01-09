from django import forms
from .models import Sketch

class SketchForm(forms.ModelForm):
     class Meta:
           model=Sketch
           fields=("caption","sketch")