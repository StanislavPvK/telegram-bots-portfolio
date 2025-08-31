from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Main menu (catalog and help)
reply_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📂 Catalog"), 
     KeyboardButton(text="ℹ️ Help")]], resize_keyboard=True)
