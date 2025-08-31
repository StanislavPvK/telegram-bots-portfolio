from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# клавиатура для покупки и возврата
def product_detail_kb(product_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Купить", callback_data=f"buy:{product_id}"), 
            InlineKeyboardButton(text="Назад", callback_data="back_to_catalog")]
        ]
    )