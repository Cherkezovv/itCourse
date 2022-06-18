from django.db import models


class Questions(models.Model):
    text = models.TextField(max_length=500)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Python Soraglar'
        verbose_name = 'Python soraglar'

    def __str__(self):
        return str(self.id)


class DjangoQuestions(models.Model):
    text = models.TextField(max_length=500)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Django Soraglar'
        verbose_name = 'Django soraglar'

    def __str__(self):
        return self.name + ".  " + self.text


class HtmlCssQuestions(models.Model):
    text = models.TextField(max_length=500)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Html&Css Soraglar'
        verbose_name = 'Html&Css soraglar'

    def __str__(self):
        return self.name + ".  " + self.text


class JavaScriptQuestions(models.Model):
    text = models.TextField(max_length=500)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'JavaScript Soraglar'
        verbose_name = 'JavaScript soraglar'

    def __str__(self):
        return self.name + ".  " + self.text


class BootstrapQuestions(models.Model):
    text = models.TextField(max_length=500)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Bootstrap Soraglar'
        verbose_name = 'Bootstrap soraglar'

    def __str__(self):
        return self.name + ".  " + self.text


class NodejsQuestions(models.Model):
    text = models.TextField(max_length=500)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Nodejs Soraglar'
        verbose_name = 'Nodejs soraglar'

    def __str__(self):
        return self.name + ".  " + self.text


