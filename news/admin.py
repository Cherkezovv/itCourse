from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]


admin.site.register(News, NewsAdmin)
