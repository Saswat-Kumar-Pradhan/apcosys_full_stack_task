from django import forms
from .models import User, Admin

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'password', 'active']
        widgets = {
            'password': forms.PasswordInput(),
        }

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['name', 'username', 'password']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())