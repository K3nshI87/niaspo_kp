# Базовый образ
FROM node:14

# Рабочая директория
WORKDIR /app

# Копируем package.json и устанавливаем зависимости
COPY package*.json ./
RUN npm install

# Копируем весь проект
COPY . .

# Открываем порт
EXPOSE 3000

# Запуск приложения
CMD ["npm", "start"]
