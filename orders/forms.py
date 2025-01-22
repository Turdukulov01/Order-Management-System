# file: orders/forms.py
from django import forms
from .models import Order


class EditOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["items"]

    def clean_items(self):
        items = self.cleaned_data.get("items")
        if not isinstance(items, dict):
            raise forms.ValidationError("Список блюд должен быть в формате JSON.")
        for item, details in items.items():
            if (
                not isinstance(details.get("price"), (int, float))
                or details["price"] <= 0
            ):
                raise forms.ValidationError(f"Неверная цена для блюда {item}.")
        return items
