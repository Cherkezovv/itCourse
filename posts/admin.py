from django.contrib import admin
from .models import Questions, DjangoQuestions, HtmlCssQuestions, JavaScriptQuestions, BootstrapQuestions, \
    NodejsQuestions


# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Questions._meta.fields]


admin.site.register(Questions, QuestionsAdmin)


class DjangoQuestionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DjangoQuestions._meta.fields]


admin.site.register(DjangoQuestions, DjangoQuestionsAdmin)


class HtmlCssQuestionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in HtmlCssQuestions._meta.fields]


admin.site.register(HtmlCssQuestions, HtmlCssQuestionsAdmin)


class JavaScriptQuestionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in JavaScriptQuestions._meta.fields]


admin.site.register(JavaScriptQuestions, JavaScriptQuestionsAdmin)


class BootstrapQuestionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BootstrapQuestions._meta.fields]


admin.site.register(BootstrapQuestions, BootstrapQuestionsAdmin)


class NodejsQuestionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NodejsQuestions._meta.fields]


admin.site.register(NodejsQuestions, NodejsQuestionsAdmin)


