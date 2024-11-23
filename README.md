# Промежуточная аттестация — Архитектор данных (1T)

Этот проект — промежуточная аттестация на Программе Архитектора данных от корпорации 1T.

## Описание

Проект представляет собой систему, которая подключается к базе данных PostgreSQL, создает таблицу, заполняет ее данными и выполняет запрос.
## Структура проекта

1. **`app.py`** — основной скрипт, который подключается к базе данных и выполняет запрос.
2. **`main.py`** — скрипт, который генерирует файл `init.sql` для инициализации базы данных.
3. **`init.sql`** — SQL-скрипт для создания таблицы и наполнения ее данными.
4. **`Dockerfile`** — файл, описывающий, как собирать образ для Python-приложения.
5. **`docker-compose.yml`** — файл для настройки и запуска сервисов (PostgreSQL и Python-приложение) с помощью Docker Compose.
6. **`requirements.txt`** — файл зависимостей Python для проекта.

## Шаги для запуска

### 1. Запуск с помощью Docker Compose

Для того чтобы запустить проект с помощью Docker, выполните следующие шаги:

1. Убедитесь, что у вас установлен [Docker](https://www.docker.com/get-started) и [Docker Compose](https://docs.docker.com/compose/install/).
2. Склонируйте этот репозиторий на вашу локальную машину.
3. Запустите команду:

   ```bash
   docker-compose up --build