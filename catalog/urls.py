from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import products_list, products_detail, contacts, home

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('catalog/', products_list, name='products_list'),
    path('products/<int:pk>/', products_detail, name='products_detail'),
    path('contacts/', contacts, name='contacts'),
]