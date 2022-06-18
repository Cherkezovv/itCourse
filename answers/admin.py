from django.contrib import admin
from .models import PythonAnswers, DjangoAnswers, HtmlCssAnswers, JavaScriptAnswers, BootstrapAnswers,  NodejsAnswers

class PythonAnswersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PythonAnswers._meta.fields]
admin.site.register(PythonAnswers, PythonAnswersAdmin)

class DjangoAnswersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DjangoAnswers._meta.fields]
admin.site.register(DjangoAnswers, DjangoAnswersAdmin)

class HtmlCssAnswersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in HtmlCssAnswers._meta.fields]
admin.site.register(HtmlCssAnswers, HtmlCssAnswersAdmin)


class JavaScriptAnswersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in JavaScriptAnswers._meta.fields]
admin.site.register(JavaScriptAnswers, JavaScriptAnswersAdmin)

class BootstrapAnswersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BootstrapAnswers._meta.fields]
admin.site.register(BootstrapAnswers, BootstrapAnswersAdmin)

class NodejsAnswersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NodejsAnswers._meta.fields]
admin.site.register(NodejsAnswers, NodejsAnswersAdmin)