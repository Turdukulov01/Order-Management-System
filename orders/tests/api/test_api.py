# file: orders/tests/test_api.py
from rest_framework.test import APITestCase
from rest_framework import status
from orders.models import Order


class OrderAPITestCase(APITestCase):
    def setUp(self):
        self.order = Order.objects.create(
            table_number=1,
            items={"dish1": {"price": 100}, "dish2": {"price": 200}},
            status="pending",
        )
        self.valid_payload = {
            "table_number": 2,
            "items": {"dish3": {"price": 150}, "dish4": {"price": 250}},
            "status": "pending",
        }

    def test_get_orders(self):
        response = self.client.get("/api/orders/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_order(self):
        response = self.client.post("/api/orders/", self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_order_status(self):
        response = self.client.patch(
            f"/api/orders/{self.order.id}/", {"status": "ready"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, "ready")

    def test_delete_order(self):
        response = self.client.delete(f"/api/orders/{self.order.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
