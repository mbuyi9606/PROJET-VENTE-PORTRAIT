from django import forms
from user.models import User

class SingupForm(forms.Form):
    class Meta:
        model = User
        fields = ["username","password"]
        widgets = {
            'username': forms.TextInput(attrs={
                'class':'input-form'
            }),
            'password': forms.TextInput(attrs={
                'class':'input-form'
            })
        }