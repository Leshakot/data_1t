# Python Pandas Docker App

Этот проект демонстрирует использование Python-приложения с библиотекой Pandas внутри Docker-контейнера. Приложение анализирует данные о сотрудниках и выводит:

- Среднюю зарплату всех сотрудников.
- Список сотрудников, которым больше 30 лет.

## Содержимое репозитория

- **`app.py`**: Основной Python-скрипт.
- **`data.csv`**: Исходные данные о сотрудниках (имя, возраст, зарплата).
- **`requirements.txt`**: Файл зависимостей для Python.
- **`Dockerfile`**: Инструкции для сборки Docker-образа.

## Пример данных

Файл `data.csv` содержит данные в следующем формате:

```csv
Name,Age,Salary
Alice,30,70000
Bob,25,50000
Charlie,35,100000
```


## Сборка Docker-образа
Для создания Docker-образа выполните команду:

```bash
docker build -t python-pandas-app .
```

## Запуск контейнера
Для запуска контейнера используйте команду:

```bash
docker run --rm python-pandas-app
```

## Ссылка на Docker Hub
https://hub.docker.com/repository/docker/leshakot/python-pandas-app/general
