from typing import Any

from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product


class HomeView(TemplateView):
    template_name = "home.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset: Any = None) -> Any:
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ContactsView(TemplateView):
    template_name = "contacts.html"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self) -> Any:
        return reverse("catalog:products_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")
