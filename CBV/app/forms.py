from .models import *
from django import forms 

class SclForm(forms.ModelForm):
    class Meta :
        model = School
        fields = '__all__'
        
