import os
from dotenv import find_dotenv, load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv(find_dotenv())

# Токен бота и ID администратора из переменных окружения
TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))