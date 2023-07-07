#syntax=docker/dockerfile:1.4

FROM python:3.10

# # Установка зависимостей
# RUN apt-get update && apt-get install -y \
#     postgresql-client

# # Создание и переход в рабочую директорию
# WORKDIR /code

# # Копирование зависимостей проекта
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt

# # Копирование остальных файлов проекта
# COPY . /code/

# # Выполнение миграций и запуск сервера Django
# # RUN python manage.py migrate

# # Определение команды для запуска сервера Django
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
