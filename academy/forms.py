from django import forms
from accounts.models import CustomUser, FranchiseDetails, TeacherDetails, TeacherLevel
from .models import Competition

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'

    pdf_file = forms.FileField(widget=forms.ClearableFileInput())
    level_cutoff_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class TeacherLevelForm(forms.ModelForm):
    prev_level_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = TeacherLevel
        fields = ['prev_level','prev_level_date']
        

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'account_type']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
       super(EditUserForm, self).__init__(*args, **kwargs)
       self.fields['password'].initial = ""

class FranchiseDetailsForm(forms.ModelForm):
    class Meta:
        model = FranchiseDetails
        exclude = ['user']
        # fields = '__all__'
        widgets = {
            'programs': forms.CheckboxSelectMultiple,
        }
    
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    # You can add custom form validation or widgets if needed
    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic if needed
        return cleaned_data
    
class TeacherDetailsForm(forms.ModelForm):
    class Meta:
        model = TeacherDetails
        exclude = ['user']
        # fields = '__all__'
    
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    # You can add custom form validation or widgets if needed
    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic if needed
        return cleaned_data