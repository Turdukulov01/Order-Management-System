# file: orders/views.py

from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Order
from orders.forms import EditOrderForm
import json


def list_orders(request):
    """
    Отображение списка заказов с фильтрацией.
    """
    status = request.GET.get("status")
    table_number = request.GET.get("table_number")
    orders = Order.objects.all()

    if status:
        orders = orders.filter(status=status)
    if table_number:
        orders = orders.filter(table_number=table_number)

    return render(request, "orders/orders_list/list_orders.html", {"orders": orders})


def add_order(request):
    """
    Создание нового заказа через веб-интерфейс.
    """
    if request.method == "POST":
        table_number = request.POST.get("table_number")
        items = request.POST.get("items")

        # Попытка декодировать JSON из текстового поля
        try:
            items = json.loads(items) if items else {}
        except json.JSONDecodeError:
            items = {}  # Если формат неверный, используем пустой словарь

        # Проверяем, что каждый элемент соответствует формату {"dish": {"price": value}}
        if isinstance(items, dict):
            valid_items = {}
            for key, value in items.items():
                if isinstance(value, dict) and "price" in value:
                    valid_items[key] = {"price": value["price"]}
                else:
                    valid_items[key] = {
                        "price": 0
                    }  # Устанавливаем цену 0 для некорректных записей
            items = valid_items

        order = Order.objects.create(table_number=table_number, items=items)
        return redirect("list_orders")
    return render(request, "orders/forms/add_order.html")


from django.shortcuts import get_object_or_404, redirect
from .models import Order


def delete_order(request, order_id):
    """
    Удаление заказа по ID.
    """
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect("list_orders")


def update_order_status(request, order_id):
    """
    Обновление статуса заказа через веб-интерфейс.
    """
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        status = request.POST.get("status")
        order.status = status
        order.save()
        return redirect("list_orders")
    return render(request, "orders/update_status.html", {"order": order})


def edit_order(request, order_id):
    """
    Редактирование заказа.
    """
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        table_number = request.POST.get("table_number")
        items = request.POST.get("items")

        # Попытка преобразовать JSON
        try:
            items = json.loads(items) if items else {}
        except json.JSONDecodeError:
            items = {}

        # Обновляем заказ
        order.table_number = table_number
        order.items = items
        order.save()
        return redirect("list_orders")

    return render(request, "orders/forms/edit_order.html", {"order": order})


def revenue_report(request):
    """
    Страница отображения выручки за смену.
    """
    revenue = Order.calculate_revenue()
    return render(request, "orders/reports/revenue_report.html", {"revenue": revenue})
