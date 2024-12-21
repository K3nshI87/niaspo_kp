# Общий Dockerfile
FROM python:3.10-slim AS backend
WORKDIR /app/backend
COPY backend ./
RUN pip install -r requirements.txt

FROM node:16 AS frontend
WORKDIR /app/frontend
COPY frontend ./
RUN npm install && npm run build

FROM postgres:13 AS db
WORKDIR /app/database
COPY database ./

# Запуск всех компонентов
CMD ["bash", "-c", "service postgresql start && cd /app/backend && python app.py && cd /app/frontend && npm start"]
