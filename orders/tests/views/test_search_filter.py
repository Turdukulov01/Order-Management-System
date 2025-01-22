# file: orders/tests/test_search_filter.py
from django.test import TestCase
from orders.models import Order


class OrderSearchFilterTest(TestCase):
    def setUp(self):
        Order.objects.create(
            table_number=1, items={"dish1": {"price": 100}}, status="pending"
        )
        Order.objects.create(
            table_number=2, items={"dish2": {"price": 200}}, status="ready"
        )
        Order.objects.create(
            table_number=3, items={"dish3": {"price": 300}}, status="paid"
        )

    def test_filter_by_status(self):
        response = self.client.get("/api/orders/", {"status": "paid"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_search_by_table_number(self):
        response = self.client.get("/api/orders/", {"search": "1"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
