# file: orders/api/views.py

from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from orders.models import Order
from orders.serializers import OrderSerializer


class OrderListCreateAPIView(generics.ListCreateAPIView):
    """
    API для создания и получения списка заказов.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["status"]  # Фильтрация по статусу
    search_fields = ["table_number"]  # Поиск по номеру стола


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API для работы с конкретным заказом (получение, обновление, удаление).
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
