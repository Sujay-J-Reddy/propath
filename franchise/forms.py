from django import forms
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        exclude = ['franchise']

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class UpdateLevelForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['programme', 'level']