from django import forms
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['id', 'name', 'dob', 'level', 'contact']

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
