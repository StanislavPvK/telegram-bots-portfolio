from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Keyboard for purchase and going back
def product_detail_kb(product_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Buy", callback_data=f"buy:{product_id}"), 
             InlineKeyboardButton(text="Back", callback_data="back_to_catalog")]
        ]
    )
