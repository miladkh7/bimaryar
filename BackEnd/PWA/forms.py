from django import forms
from .models import  TempRegister
class TempRegisterForm(forms.ModelForm):
    class Meta:
        model=TempRegister
        fields='__all__'