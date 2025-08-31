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


# Базовый URL для API CoinGecko
API_BASE_URL = "https://api.coingecko.com/api/v3"
# Список поддерживаемых криптовалют
SUPPORTED_CRYPTOS = ["bitcoin", "ethereum", "litecoin"]
