# Brendwall-product-API (Тестовое задание)
Код на сайте: https://product-api.risetime.ru
Документация API эндпоинтов Бекенда. https://product-api.risetime.ru/api/schema/

## Endpoints
* /api/products/add/ - Добавление продукта
* /api/products/list/ - Список продуктов
## Просмотр проекта на локальной машине:
Склонировать репозиторий на локальную машину:
```
git clone git@github.com:Rodyapa/Brendwall-product-API.git
```
Создать виртуальное окружение
```
python -m vevn venv 
```
Активировать виртуальное окружение
```
source venv/bin/activate
```
Установить зависимости
```
poetry install
```
Собрать статику
```
python manage.py collectstatic
```
Провести миграции
```
python manage.py makemigrations
python manage.py migrate
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

