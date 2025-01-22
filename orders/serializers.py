# file: orders/api/serializers.py
from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "table_number", "items", "total_price", "status"]
        read_only_fields = ["id", "total_price"]

    def validate_items(self, value):
        # Проверяем, что список блюд содержит только корректные данные
        if not isinstance(value, dict):
            raise serializers.ValidationError("Items must be a dictionary.")
        for item, details in value.items():
            if (
                not isinstance(details.get("price"), (int, float))
                or details["price"] <= 0
            ):
                raise serializers.ValidationError(f"Invalid price for item {item}.")
        return value
