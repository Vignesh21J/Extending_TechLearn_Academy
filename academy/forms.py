from django import forms
from .models import Trainer, Student

class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model=Trainer
        fields='__all__'

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'