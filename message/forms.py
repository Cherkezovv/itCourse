from django import forms
from .models import *


class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['subject', 'from_email', 'message']
        labels = {'subject': '', 'from_email': '', 'message': ''}
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': ' Subject', 'class': 'form-control'}),
            'from_email': forms.TextInput(attrs={'placeholder': ' E-mail', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'cols': 80, 'placeholder': ' Message', 'class': 'form-control'}),
        }
