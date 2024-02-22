# myapp/forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class HomeForm(forms.Form):
    # Add fields for HomeForm
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    # Add more fields as needed for your HomeForm
