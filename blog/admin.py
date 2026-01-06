from django.contrib import admin

from blog.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "created_at", "publication_flag")
    list_filter = ("title", "created_at", "publication_flag")
    search_fields = ("title", "created_at", "publication_flag")
