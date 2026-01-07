from typing import Any

from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок записи")
    content = models.CharField(max_length=1000, verbose_name="Содержимое записи")
    preview = models.ImageField(upload_to="blog/image", blank=True, null=True, verbose_name="Превью записи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    publication_flag = models.BooleanField(default=False, verbose_name="Признак публикации")
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров", help_text="Укажите количество просмотров", default=0
    )

    class Meta:
        verbose_name = "Заголовок записи"
        verbose_name_plural = "Заголовки записей"
        ordering = ["title", "publication_flag", "created_at", "views_counter"]

    def __str__(self) -> Any:
        return self.title

    @property
    def get_content(self) -> Any:
        if len(self.content) < 100:
            return self.content
        return f"{self.content[:97]}..."
