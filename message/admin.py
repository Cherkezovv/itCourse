from django.contrib import admin
from .models import Messages


class MessagesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Messages._meta.fields]

admin.site.register(Messages, MessagesAdmin)
