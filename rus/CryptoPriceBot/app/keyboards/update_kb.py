from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Генерация клавиатуры с кнопкой обновления цены для конкретной криптовалюты
def update_kb(crypto: str):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔄 Обновить", callback_data=f"update_{crypto}")]
        ]
    )