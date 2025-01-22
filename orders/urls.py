# file: orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_orders, name="list_orders"),  # Имя маршрута: list_orders
    path("add/", views.add_order, name="add_order"),
    path("<int:order_id>/edit/", views.edit_order, name="edit_order"),
    path("<int:order_id>/delete/", views.delete_order, name="delete_order"),
    path(
        "<int:order_id>/update_status/",
        views.update_order_status,
        name="update_order_status",
    ),
    path("revenue/", views.revenue_report, name="revenue_report"),
]
