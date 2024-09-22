# Brendwall-product-API (Тестовое задание)
Реализация доступна на сайте: https://product-api.risetime.ru
Документация API эндпоинтов Бекенда. https://product-api.risetime.ru/api/schema/

## Endpoints
* /api/products/add/ - Добавление продукта
* /api/products/list/ - Список продуктов
## Просмотр проекта на локальной машине:
Склонировать репозиторий на локальную машину:
```
git clone git@github.com:Rodyapa/Brendwall-product-API.git
```
Перейти в директорию с кодом бекенда
```
cd Brendwall-product-API/backend
```
Создать виртуальное окружение
```
python3 -m vevn venv 
```
Активировать виртуальное окружение
```
source venv/bin/activate
```
Установить пакетный менеджер Poetry: https://python-poetry.org/docs/
Установить зависимости
```
poetry install 
```
Или установите зависимости с помощью pip
```
pip install -r requirements.txt
```
```
Собрать статику
```
python brendwall_product/manage.py collectstatic
```
Провести миграции
```
python brendwall_product/manage.py makemigrations
python brendwall_product/manage.py migrate
```
Запустить локальный сервер
```
python manage.py runserver
```

## Технологии:
    *Python
    *Django
    *Django REST framework
    *Poetry

