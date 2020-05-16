from django import forms
from django.contrib.auth.forms import UserCreationForm, \
    AuthenticationForm, UserChangeForm
from .models import User


class LoginForm(AuthenticationForm):
    model = User


class RegisterForm(UserCreationForm):
    model = User

    firstname = forms.CharField(label='First name', max_length=50)
    username = forms.CharField(label='Username', max_length=50)
    email = forms.EmailField()

    class Meta:
        """Fields to include on the form"""
        fields = ('firstname', 'username', 'email')
        model = User


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')
