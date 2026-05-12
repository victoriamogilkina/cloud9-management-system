from django import forms
from .models import Clients

class PostClient(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('full_name', 'pc_number', 'expires_at')

