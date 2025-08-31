from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Generate a keyboard with a "Refresh Price" button for a specific cryptocurrency
def update_kb(crypto: str):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔄 Refresh", callback_data=f"update_{crypto}")]
        ]
    )