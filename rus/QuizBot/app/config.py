"""
Модуль конфигурации для бота.

Загружает переменные окружения из .env файла и проверяет наличие обязательного токена.
"""


import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("Не найден TOKEN в .env файле!")