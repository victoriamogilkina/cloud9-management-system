from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Users
from django import forms

class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = Users
        fields = ['username', 'role']

class MyLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()