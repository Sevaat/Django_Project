from typing import Any

from django.core.cache import cache
from django.db.models import QuerySet

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_cache() -> QuerySet[Product]:
    """Получение данных из кэша или запись данных в кэш об опубликованных продуктах"""
    if not CACHE_ENABLED:
        return Product.objects.filter(publication_flag=True)
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.filter(publication_flag=True)
    cache.set(key, products)
    return products

def get_products_by_category(category_id: int) -> QuerySet[Product]:
    """Возвращает список опубликованных продуктов указанной категории"""
    products = Product.objects.filter(
        publication_flag=True, category_id=category_id
    )

    if not CACHE_ENABLED:
        return products

    key = f"products_list_category_{category_id}"
    if cached_products := cache.get(key):
        return cached_products

    cache.set(key, products)

    return products
