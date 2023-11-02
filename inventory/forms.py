from django import forms
from django.forms import formset_factory
from .models import Vendor, Item

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'contact', 'location']

class LogEntryForm(forms.Form):
    vendor = forms.IntegerField()
    date = forms.DateField()
    items = forms.JSONField()



