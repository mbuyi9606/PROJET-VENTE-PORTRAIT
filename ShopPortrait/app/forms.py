from django import forms
from app.models import Portrait

class PortraitForm(forms.ModelForm):
    class Meta:
        model = Portrait
        fields = ["titre","description","image"]
        widgets = {
            'titre': forms.TextInput(attrs={
                'class':"input-form"
            }),
            'image': forms.FileInput(attrs={
                'class':"input-form",
                'accept':'image/*'
            }),
            'description': forms.TextInput(attrs={
                'class':"descripiton-form"
            })
        }