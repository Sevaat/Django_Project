from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product


class HomeView(TemplateView):
    template_name = "home.html"


class ProductListView(ListView):
    model = Product

    def get_queryset(self) -> Any:
        return Product.objects.filter(publication_flag=True)


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset: Any = None) -> Any:
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ContactsView(TemplateView):
    template_name = "contacts.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = "users:login"
    redirect_field_name = "next"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "users:login"
    redirect_field_name = "next"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self) -> Any:
        return reverse("catalog:products_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "users:login"
    redirect_field_name = "next"
    model = Product
    success_url = reverse_lazy("catalog:products_list")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        user = self.request.user
        if obj.owner != user and not user.has_perm("catalog.can_delete_product"):
            raise PermissionDenied
        return obj
