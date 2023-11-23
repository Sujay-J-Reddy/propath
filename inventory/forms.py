from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Vendor, Item

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'contact', 'location']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'qty', 'last_purchase_price', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class LogEntryForm(forms.Form):
    vendor = forms.IntegerField()
    date = forms.DateField()
    items = forms.JSONField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
