# Order Management System

## Описание
Веб-приложение для управления заказами в кафе. Позволяет добавлять, редактировать, удалять заказы, а также отображать и фильтровать их. Реализован подсчет общей выручки за смену.

---

## Функционал
- Добавление заказов с указанием номера стола и списка блюд.
- Редактирование заказов.
- Удаление заказов.
- Фильтрация заказов по статусу и номеру стола.
- Изменение статуса заказа (в ожидании, готово, оплачено).
- Подсчет общей выручки за оплаченные заказы.
- REST API для работы с заказами.

---

## Технологии
- Python 3.8+
- Django 4+
- SQLite (или PostgreSQL)
- HTML/CSS

---

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-репозиторий/order-management-system.git
   cd order-management-system
   
Создайте виртуальное окружение:
python -m venv venv
source venv/bin/activate   # для Linux/MacOS
venv\Scripts\activate      # для Windows

Установите зависимости:
pip install -r requirements.txt

Примените миграции:
python manage.py migrate

Запустите сервер разработки:
python manage.py runserver

Перейдите в браузере по адресу:
http://127.0.0.1:8000

API
GET /api/orders/ — получить список заказов.
POST /api/orders/ — создать новый заказ.
GET /api/orders/<id>/ — получить детали заказа.
PUT /api/orders/<id>/ — обновить заказ.
DELETE /api/orders/<id>/ — удалить заказ.

Auhtor: Turdukulov01
