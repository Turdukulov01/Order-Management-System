# file: orders/tests.py
from django.test import TestCase
from ..models import Order


class OrderModelTest(TestCase):
    def setUp(self):
        # Создаем тестовые заказы
        self.order1 = Order.objects.create(
            table_number=1,
            items={"dish1": {"price": 100}, "dish2": {"price": 200}},
            status="pending",
        )
        self.order2 = Order.objects.create(
            table_number=2,
            items={"dish1": {"price": 50}, "dish2": {"price": 150}},
            status="paid",
        )

    def test_order_creation(self):
        """Тест создания заказа и расчета стоимости."""
        self.assertEqual(self.order1.total_price, 300)
        self.assertEqual(self.order2.total_price, 200)

    def test_order_status_update(self):
        """Тест обновления статуса заказа."""
        self.order1.status = "ready"
        self.order1.save()
        self.assertEqual(self.order1.status, "ready")

    def test_order_deletion(self):
        """Тест удаления заказа."""
        order_id = self.order1.id
        self.order1.delete()
        with self.assertRaises(Order.DoesNotExist):
            Order.objects.get(id=order_id)

    def test_calculate_revenue(self):
        """Тест расчета выручки."""
        revenue = Order.calculate_revenue()
        self.assertEqual(revenue, 200)
