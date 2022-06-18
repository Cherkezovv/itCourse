from django.db import models
from posts.models import Questions, DjangoQuestions, HtmlCssQuestions, JavaScriptQuestions, BootstrapQuestions, \
    NodejsQuestions


class PythonAnswers(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE, null=True, default=1)
    text = models.TextField(max_length=500, null=False)
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(blank=True, null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Python Jogaplar'
        verbose_name = 'Python Jogaplar'


class DjangoAnswers(models.Model):
    django_question = models.ForeignKey(DjangoQuestions, on_delete=models.CASCADE, null=True, default=1)
    text = models.TextField(max_length=500)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Django Jogaplar'
        verbose_name = 'Django Jogaplar'


class HtmlCssAnswers(models.Model):
    htmlcss_question = models.ForeignKey(HtmlCssQuestions, on_delete=models.CASCADE, null=True, default=1)
    text = models.TextField(max_length=500)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Html&Css Jogaplar'
        verbose_name = 'Html&Css Jogaplar'


class JavaScriptAnswers(models.Model):
    javascript_question = models.ForeignKey(JavaScriptQuestions, on_delete=models.CASCADE, null=True, default=1)
    text = models.TextField(max_length=500)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'JavaScript Jogaplar'
        verbose_name = 'JavaScript Jogaplar'


class BootstrapAnswers(models.Model):
    bootstrap_question = models.ForeignKey(BootstrapQuestions, on_delete=models.CASCADE, null=True, default=1)
    text = models.TextField(max_length=500)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Bootstrap Jogaplar'
        verbose_name = 'Bootstrap Jogaplar'


class NodejsAnswers(models.Model):
    nodejs_question = models.ForeignKey(NodejsQuestions, on_delete=models.CASCADE, null=True, default=1)
    text = models.TextField(max_length=500)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Nodejs Jogaplar'
        verbose_name = 'Nodejs Jogaplar'
