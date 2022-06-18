from django import forms
from .models import PythonAnswers, DjangoAnswers, HtmlCssAnswers, JavaScriptAnswers, BootstrapAnswers,  NodejsAnswers


class PythonAnswersForm(forms.ModelForm):
    class Meta:
        model = PythonAnswers
        fields = ['text', 'name', 'email']
        labels = { 'text': '', 'name': '', 'email': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80, 'placeholder': ' Write your answers!', 'class': 'form-control'}),
                   'name': forms.TextInput(attrs={'placeholder': ' Your Name', 'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'placeholder': ' E-mail', 'class': 'form-control'}),
                   }


class DjangoAnswersForm(forms.ModelForm):
    class Meta:
        model = DjangoAnswers
        fields = ['text', 'name', 'email']
        labels = {'text': '', 'name': '', 'email': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80, 'placeholder': ' Write your answers!', 'class': 'form-control'}),
                   'name': forms.TextInput(attrs={'placeholder': ' Name', 'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'placeholder': ' E-mail', 'class': 'form-control'}),
                   }


class HtmlCssAnswersForm(forms.ModelForm):
    class Meta:
        model = HtmlCssAnswers
        fields = ['text', 'name', 'email']
        labels = {'text': '', 'name': '', 'email': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80, 'placeholder': ' Write your answers!', 'class': 'form-control'}),
                   'name': forms.TextInput(attrs={'placeholder': ' Name', 'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'placeholder': ' E-mail', 'class': 'form-control'}),
                   }

class JavaScriptAnswersForm(forms.ModelForm):
    class Meta:
        model = JavaScriptAnswers
        fields = ['text', 'name', 'email']
        labels = {'text': '', 'name': '', 'email': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80, 'placeholder': ' Write your answers!', 'class': 'form-control'}),
                   'name': forms.TextInput(attrs={'placeholder': ' Name', 'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'placeholder': ' E-mail', 'class': 'form-control'}),
                   }


class BootstrapAnswersForm(forms.ModelForm):
    class Meta:
        model = BootstrapAnswers
        fields = [ 'text', 'name', 'email']
        labels = {'text': '', 'name': '', 'email': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80, 'placeholder': ' Write your answers!', 'class': 'form-control'}),
                   'name': forms.TextInput(attrs={'placeholder': ' Name', 'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'placeholder': ' E-mail', 'class': 'form-control'}),
                   }


class NodejsAnswersForm(forms.ModelForm):
    class Meta:
        model = NodejsAnswers
        fields = ['text', 'name', 'email']
        labels = {'text': '', 'name': '', 'email': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80, 'placeholder': ' Write your answers!', 'class': 'form-control'}),
                   'name': forms.TextInput(attrs={'placeholder': ' Name', 'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'placeholder': ' E-mail', 'class': 'form-control'}),
                   }