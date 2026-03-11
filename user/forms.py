from django.forms import ModelForm
from django.contrib.auth.models import User

# This class is for User form on user profile
class UserDataForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']