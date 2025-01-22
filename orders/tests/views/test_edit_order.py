# file: orders/tests/test_edit_order.py
from django.test import TestCase
from django.urls import reverse
from orders.models import Order


class EditOrderTest(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            table_number=1,
            items={"dish1": {"price": 100}, "dish2": {"price": 200}},
            status="pending",
        )

    def test_edit_order_get(self):
        response = self.client.get(reverse("edit_order", args=[self.order.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_order_post(self):
        new_items = {"dish1": {"price": 150}, "dish3": {"price": 300}}
        response = self.client.post(
            reverse("edit_order", args=[self.order.id]),
            {"items": new_items},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 302)
        self.order.refresh_from_db()
        self.assertEqual(self.order.items, new_items)
