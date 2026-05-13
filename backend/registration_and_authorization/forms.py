from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Users
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ["username", "role"]

class MyLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "border-3 border-gray-300 bg-gray-100 shadow-xl transition-transform focus:bg-gray-200 focus:scale-105 focus:shadow-gray-400 outline-0 rounded-xl px-4 py-2 mt-2 w-full ",
                "placeholder": "Enter username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "border-3 border-gray-300 bg-gray-100 shadow-xl transition-transform focus:bg-gray-200 focus:scale-105 focus:shadow-gray-400 outline-0 rounded-xl px-4 py-2 mt-2 w-full ",
                "placeholder": "Enter password"
            }
        )
    )
