from django import forms
from .models import Assignment399


class Assignment399Form(forms.ModelForm):
    class Meta:
        model = Assignment399
        fields = '__all__'
