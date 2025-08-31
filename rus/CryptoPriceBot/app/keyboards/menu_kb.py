from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.config import SUPPORTED_CRYPTOS


# Клавиатура с кнопками для каждой поддерживаемой криптовалюты
menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=crypto.upper(), callback_data=crypto) 
        for crypto in SUPPORTED_CRYPTOS]
    ]
)

