from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.config import SUPPORTED_CRYPTOS


# Keyboard with buttons for each supported cryptocurrency
menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=crypto.upper(), callback_data=crypto) 
        for crypto in SUPPORTED_CRYPTOS]
    ]
)