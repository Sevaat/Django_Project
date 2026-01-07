from django.urls import path

from blog.apps import BlogConfig
from blog.views import NoteCreateView, NoteDeleteView, NoteDetailView, NoteListView, NoteUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path("", NoteListView.as_view(), name="notes_list"),
    path("<int:pk>/", NoteDetailView.as_view(), name="notes_detail"),
    path("create/", NoteCreateView.as_view(), name="notes_create"),
    path("<int:pk>/update/", NoteUpdateView.as_view(), name="notes_update"),
    path("<int:pk>/delete/", NoteDeleteView.as_view(), name="notes_delete"),
]
