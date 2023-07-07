#syntax=docker/dockerfile:1.4

# FROM --platform=$BUILDPLATFORM python:3.7-alpine AS builder
# EXPOSE 8000
# WORKDIR /app 
# COPY requirements.txt /app
# RUN pip3 install -r requirements.txt --no-cache-dir
# COPY . /app 
# ENTRYPOINT ["python3"] 
# CMD ["manage.py", "runserver", "0.0.0.0:8000"]

# FROM builder as dev-envs
# RUN <<EOF
# apk update
# apk add git
# EOF

# RUN <<EOF
# addgroup -S docker
# adduser -S --shell /bin/bash --ingroup docker vscode
# EOF
# # install Docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /
# CMD ["manage.py", "runserver", "0.0.0.0:8000"]
# Базовый образ
FROM python:3.9

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    postgresql-client

# Создание и переход в рабочую директорию
WORKDIR /code

# Копирование зависимостей проекта
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Копирование остальных файлов проекта
COPY . /code/

# Выполнение миграций и запуск сервера Django
# RUN python manage.py migrate

# Определение команды для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
