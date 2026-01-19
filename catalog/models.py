from typing import Any

from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование категории")
    description = models.CharField(max_length=500, verbose_name="Описание категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self) -> Any:
        return self.name

    @property
    def get_description(self) -> Any:
        if len(self.description) < 100:
            return self.description
        return f"{self.description[:97]}..."


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование продукта")
    description = models.CharField(max_length=500, verbose_name="Описание продукта")
    image = models.ImageField(upload_to="product/photo", blank=True, null=True, verbose_name="Изображение продукта")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Категория продукта",
        related_name="catalog",
    )
    price = models.CharField(max_length=50, verbose_name="Стоимость продукта")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата изготовления (создания) продукта")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения продукта")
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров", help_text="Укажите количество просмотров", default=0
    )
    publication_flag = models.BooleanField(default=False, verbose_name="Признак публикации")
    owner = models.ForeignKey(User, verbose_name="Владелец", help_text="Укажите владельца продукта", blank=True, null=True, on_delete=models.SET_NULL)

    @property
    def get_description(self) -> Any:
        if len(self.description) < 100:
            return self.description
        return f"{self.description[:97]}..."

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price", "created_at", "updated_at"]
        permissions = [
            ("can_unpublish_product", "Can edit publication flag"),
            ("can_delete_product", "Can delete flag"),
        ]

    def __str__(self) -> Any:
        return self.name
