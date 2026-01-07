from typing import Any

from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blog.models import Note


class NoteListView(ListView):
    model = Note

    def get_queryset(self) -> Any:
        return Note.objects.filter(publication_flag=True)


class NoteDetailView(DetailView):
    model = Note

    def get_object(self, queryset=None) -> Any:
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class NoteCreateView(CreateView):
    model = Note
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("blog:notes_list")


class NoteUpdateView(UpdateView):
    model = Note
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("blog:notes_list")

    def get_success_url(self) -> Any:
        return reverse("blog:notes_detail", args=[self.kwargs.get("pk")])


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy("blog:notes_list")
