from django import forms
from catalog.models import Product

BANNED_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description", "image", "category", "price")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.fields["image"].widget.attrs["class"] = "form-control-file"
        self.fields["name"].widget.attrs["placeholder"] = "Введите название продукта"
        self.fields["description"].widget.attrs["placeholder"] = "Введите описание продукта"


    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        lower = name.lower()
        if any(word in lower for word in BANNED_WORDS):
            raise forms.ValidationError(
                "Название содержит запрещённые слова."
            )
        return name


    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        lower = description.lower()
        if any(word in lower for word in BANNED_WORDS):
            raise forms.ValidationError(
                "Описание содержит запрещённые слова."
            )
        return description


    def clean_price(self):
        price = self.cleaned_data.get("price")
        price = price.replace(",", ".")
        price = price.replace(" ", "")

        if ProductForm.can_convert_to_float(price):
            price = float(price)
            if price >= 0:
                return price
        raise forms.ValidationError("Цена продукта введена некорректно.")

    @staticmethod
    def can_convert_to_float(s):
        """Проверка возможности конвертации в float"""
        try:
            float(s)
            return True
        except (ValueError, TypeError):
            return False