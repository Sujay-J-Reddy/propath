from django import forms
from accounts.models import CustomUser, FranchiseDetails, TeacherDetails, TeacherLevel
from .models import Competition

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'

    pdf_file = forms.FileField(widget=forms.ClearableFileInput())
    level_cutoff_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from crispy_forms.layout import Layout, Div, Field

class TeacherLevelForm(forms.ModelForm):
    prev_level_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = TeacherLevel
        fields = ['prev_level','prev_level_date']
        

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'account_type']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper(self)
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Submit'))
            self.helper.layout = Layout(
            Div(
                'username',
                css_class='form-outline mb-4',
                data_mdb_input_init=True
            ),
            Div(
                'password',
                css_class='form-outline mb-4',
                data_mdb_input_init=True
            ),
            'account_type'
        )

      

   

        # self.fields['username'].widget.attrs.update({
        #     'class': 'form-control',  # Add Bootstrap class
        #     'placeholder': 'Enter your username',  # Placeholder text
        #     'autocomplete': 'off',  # Disable autocomplete (optional)
        #     # You can add other attributes as needed
        # })

class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'id': 'form1Example1',
            'placeholder': 'Username',
        })

        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'form1Example2',
            'placeholder': 'Password',
        })

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