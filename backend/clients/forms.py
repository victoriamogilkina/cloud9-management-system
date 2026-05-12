from django import forms
from .models import Clients

class PostClient(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('full_name', 'pc_number', 'expires_at')
        widgets = {
            "expires_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

class AddTime(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('expires_at',)
        widgets = {
            "expires_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }