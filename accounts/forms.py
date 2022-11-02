from dataclasses import field
from django import forms

from accounts.models import User  

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"