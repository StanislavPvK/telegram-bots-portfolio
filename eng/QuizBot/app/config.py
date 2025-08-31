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
