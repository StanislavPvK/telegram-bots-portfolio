"""
Configuration module for the bot.

Loads environment variables from the .env file and checks for the required token.
"""

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN not found in the .env file!")


# Base URL for the CoinGecko API
API_BASE_URL = "https://api.coingecko.com/api/v3"
# List of supported cryptocurrencies
SUPPORTED_CRYPTOS = ["bitcoin", "ethereum", "litecoin"]
