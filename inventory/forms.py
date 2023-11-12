from django import forms
from .models import Vendor, Item

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'contact', 'location']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'qty']

class LogEntryForm(forms.Form):
    vendor = forms.IntegerField()
    date = forms.DateField()
    items = forms.JSONField()



