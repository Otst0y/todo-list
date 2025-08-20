from django.contrib import admin

from todos.models import Task, Tag

admin.site.register(Task)
admin.site.register(Tag)
