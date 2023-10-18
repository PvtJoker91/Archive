from django import forms
from .models import *


class SearchForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['second_name', 'name', 'third_name', 'passport']
