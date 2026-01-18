from typing import Any

from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def  get_products_cache() -> Any:
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