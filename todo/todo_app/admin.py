from django.contrib import admin

from todo_app.apps import TodoAppConfig
from todo_app.models import ToDoList


class ToDoAdmin(admin.ModelAdmin):
    list_display = ['title', 'context', 'is_done', 'is_today']
    list_editable = ['is_done']


admin.site.register(ToDoList, ToDoAdmin)
