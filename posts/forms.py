from django import forms
from .models import Questions, DjangoQuestions, HtmlCssQuestions, JavaScriptQuestions, BootstrapQuestions, \
    NodejsQuestions


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['name', 'email', 'text']
        labels = {'text': '', 'name': '', 'email': ''}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'placeholder': ' Write your question!', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': ' Name', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': ' E-mail', 'class': 'form-control'}),
        }


class DjangoQuestionsForm(forms.ModelForm):
    class Meta:
        model = DjangoQuestions
        fields = ['name', 'email', 'text']
        labels = {'text': '', 'name': '', 'email': ''}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'placeholder': ' Write your question!', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': ' Name', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': ' E-mail', 'class': 'form-control'}),
        }


class HtmlCssQuestionsForm(forms.ModelForm):
    class Meta:
        model = HtmlCssQuestions
        fields = ['name', 'email', 'text']
        labels = {'text': '', 'name': '', 'email': ''}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'placeholder': ' Write your question!', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': ' Name', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': ' E-mail', 'class': 'form-control'}),
        }


class JavaScriptQuestionsForm(forms.ModelForm):
    class Meta:
        model = JavaScriptQuestions
        fields = ['name', 'email', 'text']
        labels = {'text': '', 'name': '', 'email': ''}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'placeholder': ' Write your question!', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': ' Name', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': ' E-mail', 'class': 'form-control'}),
        }


class BootstrapQuestionsForm(forms.ModelForm):
    class Meta:
        model = BootstrapQuestions
        fields = ['name', 'email', 'text']
        labels = {'text': '', 'name': '', 'email': ''}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'placeholder': ' Write your question!', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': ' Name', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': ' E-mail', 'class': 'form-control'}),
        }


class NodejsQuestionsForm(forms.ModelForm):
    class Meta:
        model = NodejsQuestions
        fields = ['name', 'email', 'text']
        labels = {'text': '', 'name': '', 'email': ''}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'placeholder': ' Write your question!', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': ' Name', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': ' E-mail', 'class': 'form-control'}),
        }
