# Cash Flows

## Описание

Cash Flows — это Django-приложение для учета финансовых транзакций с поддержкой статусов, типов, категорий и подкатегорий.

Весь функционал находится в админке. Есть фикстуры, если потребуется можете загрузить.

## Требования

- Python 3.11+
- Django 5.2.1
- asgiref==3.8.1
- sqlparse==0.5.3

Установить зависимости можно командой:

```
pip install -r requirements.txt
```

## Быстрый старт

1. Клонируйте репозиторий и перейдите в папку проекта:

   ```
   git clone https://github.com/fourvleg/taskproject2.git
   cd taskproject2
   ```

2. Установите зависимости:

   ```
   pip install -r requirements.txt
   ```

3. Примените миграции:

   ```
   python manage.py migrate
   ```

4. Создайте суперпользователя:

   ```
   python manage.py createsuperuser
   ```

5. Загрузите фикстуры:

   ```
   python manage.py loaddata initial_data.json
   ```

6. Запустите сервер разработки:

   ```
   python manage.py runserver
   ```

7. Перейдите в админ-панель: http://127.0.0.1:8000/admin/
