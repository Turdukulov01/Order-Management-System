# file: orders/tests/test_revenue_report.py
from django.test import TestCase
from django.urls import reverse
from orders.models import Order


class RevenueReportTest(TestCase):
    def setUp(self):
        Order.objects.create(
            table_number=1,
            items={"dish1": {"price": 100}, "dish2": {"price": 200}},
            status="paid",
        )
        Order.objects.create(
            table_number=2,
            items={"dish3": {"price": 150}, "dish4": {"price": 250}},
            status="pending",
        )

    def test_revenue_report_view(self):
        response = self.client.get(reverse("revenue_report"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "300 руб.")
