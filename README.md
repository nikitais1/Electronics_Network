# Electronics Network

## Описание
Веб-приложение для управления сетью по продаже электроники. Приложение включает админ-панель для управления объектами сети и API-интерфейс для взаимодействия с данными.

## Основные функции
- Иерархическая структура сети по продаже электроники:
  - Завод
  - Розничная сеть
  - Индивидуальный предприниматель
- Поддержка контактов и продуктов для каждого звена сети
- Админ-панель с фильтрацией, ссылками на поставщиков и возможностью очистки задолженности
- API с CRUD операциями и фильтрацией

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <repo_url>
   cd electronics_network
   ```
2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv venv
   env\Scripts\activate  # Для Windows
   ```
3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
4. Примените миграции:
    ```bash
    python manage.py migrate
    ```
5. Создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```
6. Запустите сервер:
    ```bash
    python manage.py runserver
    ```



## Использование
### Админ-панель
Админ-панель доступна по адресу http://127.0.0.1:8000/admin/. Войдите с учетными данными суперпользователя для управления объектами сети.

### API
API доступно по адресу http://127.0.0.1:8000/api/nodes/.

### Примеры запросов
* Получить список всех объектов сети:

```http
GET /api/nodes/
```
* Создать новый объект сети:

```http
POST /api/nodes/
Content-Type: application/json
{
  "name": "Новая сеть",
  "email": "email@example.com",
  "country": "Россия",
  "city": "Москва",
  "street": "Улица Ленина",
  "house_number": "10",
  "level": 1,
  "supplier": 1,
  "debt": 1000.00
}
```
* Фильтрация объектов по стране:

```http
GET /api/nodes/?country=Россия
```
### Права доступа
* Только активные сотрудники могут получить доступ к API. Убедитесь, что учетные записи сотрудников активированы в админ-панели.

## Структура проекта
```plaintext
electronics_sales/
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── electronics_network/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├──env/
│
├── users/
│   ├── management/
│   │   ├── commands/
│   │   │   ├── __init__.py
│   │   │   └── csu.py
│   │   └── __init__.py
│   │
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── service.py
│   ├── urls.py
│   └── views.py
│
├── .env
├── .env.sample
├── .gitignore
├── docker-compose.yaml
├── Dockerfile
├── LICENSE
├── manage.py
├── README.md
└── requirements.txt
```

## Требования
* Python 3.8+
* Django 3+
* DRF 3.10+
* PostgreSQL 10+

## Лицензия
CC0 1.0 Universal

## Docker
Запуск проекта через Docker:
* Изменить в файле .env значение POSTGRES_HOST с 127.0.0.1 на db
* Соберите образы:
```bash
docker-compose build
```
* Запустите контейнеры:
```bash
docker-compose up
```
Общая команда:
```bash
docker-compose up -d --build
```




