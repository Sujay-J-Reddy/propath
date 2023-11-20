from django import forms
from accounts.models import Admin, Franchisee

class FranchiseeForm(forms.ModelForm):
    class Meta:
        model = Franchisee
        fields = ['username', 'password', 'location', 'contact']


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['username', 'password']