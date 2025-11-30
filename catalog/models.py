from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование категории")
    description = models.CharField(max_length=500, verbose_name="Описание категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование продукта")
    description = models.CharField(max_length=500, verbose_name="Описание продукта")
    image = models.ImageField(upload_to='product/photo', blank=True, null=True, verbose_name="Изображение продукта")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Категория продукта", related_name="products")
    price = models.CharField(max_length=50, verbose_name="Стоимость продукта")
    production_date = models.DateField(verbose_name="Дата изготовления (создания) продукта")
    last_modified_date = models.DateTimeField(verbose_name="Дата последнего изменения продукта")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['name', 'category', 'price', 'production_date', 'last_modified_date']

    def __str__(self):
        return self.name