FROM python:3.9-alpine

# Копируем файлы приложения
COPY . /app
WORKDIR /app

# Экспонируем порт
EXPOSE 8080

# Запускаем приложение
CMD ["python", "app.py"]
