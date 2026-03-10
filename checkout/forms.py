from django import forms

class PurchaseForm(forms.Form):
    address = forms.CharField(max_length=200, label='Address')
    zip_code = forms.IntegerField(label='Zip Code')
    province = forms.CharField(max_length=200, label='Province')
    phone = forms.IntegerField(label='Phone')
    