from django import forms

class UserDataForm(forms.Form):
    first_name = forms.CharField(max_length=200, label='First Name')
    last_name = forms.CharField(max_length=200, label='Last Name')
    email = forms.EmailField(label='Email')