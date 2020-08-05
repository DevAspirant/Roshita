from django import forms
from .models import *

class RoshitaForm(forms.ModelForm):
    class Meta:
        model = Roshita
        fields =('title',)


