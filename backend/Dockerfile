# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем psycopg2 для работы с PostgreSQL
RUN pip install psycopg2-binary

# Копируем код в контейнер
COPY . .

# Экспонируем порт 5000 для Flask
EXPOSE 5000

# Запускаем приложение
CMD ["python", "app.py"]
