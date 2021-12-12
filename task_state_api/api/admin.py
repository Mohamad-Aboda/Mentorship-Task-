from django.contrib import admin

from .models import Task

@admin.register(Task)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "state")
    list_filter = ("state",)
    search_fields = ("title", )
