from django import forms
from accounts.models import CustomUser, FranchiseDetails

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
    
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    # You can add custom form validation or widgets if needed
    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic if needed
        return cleaned_data