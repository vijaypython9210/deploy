from django import forms
from .models import start

class MyForm(forms.ModelForm):
    class Meta:
        model=start
        fields='__all__'