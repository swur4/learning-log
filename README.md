# Learning Log

Веб-приложение для ведения личного журнала обучения. Пользователи могут регистрироваться, создавать темы и добавлять к ним записи.

## Технологии

- Python 3.12
- Django
- SQLite
- Bootstrap 4
- Gunicorn
- WhiteNoise
- Docker и Docker Compose

## Возможности

- Регистрация и авторизация пользователей.
- Создание и просмотр тем.
- Добавление и редактирование записей.
- Раздельное хранение тем и записей пользователей.
- Административная панель Django.

## Локальный запуск

1. Клонировать репозиторий:

   ```bash
   git clone https://github.com/swur4/learning-log.git
   cd learning-log
   ```

2. Создать виртуальное окружение:

   ```bash
   python -m venv ll_env
   ```

3. Активировать окружение и установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Создать файл `.env` и задать переменные окружения:

   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   APP_PORT=8000
   ```

5. Выполнить миграции:

   ```bash
   python manage.py migrate
   ```

6. Запустить сервер:

   ```bash
   python manage.py runserver
   ```

## Запуск через Docker Compose

1. Создать файл `.env` с необходимыми переменными окружения.
2. Выполнить команду:

   ```bash
   docker compose up -d --build
   ```

3. Приложение будет доступно по адресу `http://localhost:8000`.

## Проверка тестов

```bash
python manage.py test
```

## Структура проекта

- `learning_log/` — настройки и конфигурация Django.
- `learning_logs/` — основное приложение с темами и записями.
- `users/` — регистрация и авторизация.
- `Dockerfile` — сборка Docker-образа.
- `compose.yaml` — конфигурация Docker Compose.
- `requirements.txt` — зависимости проекта.

## Безопасность

Файл `.env`, база данных и виртуальное окружение не входят в репозиторий. Секретные ключи и пароли не публикуются.