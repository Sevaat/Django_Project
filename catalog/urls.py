from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, contacts, home, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('catalog/', ProductListView.as_view(), name='products_list'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/create', ProductCreateView.as_view(), name='products_create'),
    path('catalog/<int:pk>/update', ProductUpdateView.as_view(), name='products_update'),
    path('catalog/<int:pk>/delete', ProductDeleteView.as_view(), name='products_delete'),
]