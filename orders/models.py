# file: orders/models.py
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Sum


class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "В ожидании"),
        ("ready", "Готово"),
        ("paid", "Оплачено"),
    ]
    table_number = models.PositiveIntegerField("Номер стола")
    items = models.JSONField("Список блюд", default=dict)
    total_price = models.DecimalField(
        "Общая стоимость", max_digits=10, decimal_places=2, default=0
    )
    status = models.CharField(
        "Статус", max_length=20, choices=STATUS_CHOICES, default="pending"
    )

    def save(self, *args, **kwargs):
        if not isinstance(self.items, dict):
            self.items = (
                {}
            )  # Установить пустой словарь, если items не является словарем
        self.total_price = sum(item.get("price", 0) for item in self.items.values())
        super().save(*args, **kwargs)

    @staticmethod
    def calculate_revenue():
        return (
            Order.objects.filter(status="paid").aggregate(revenue=Sum("total_price"))[
                "revenue"
            ]
            or 0
        )

    def __str__(self):
        return f"Заказ {self.id} (стол {self.table_number})"
