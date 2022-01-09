from django import forms
from froala_editor.widgets import FroalaEditor

from .models import *


class blogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['m_content']