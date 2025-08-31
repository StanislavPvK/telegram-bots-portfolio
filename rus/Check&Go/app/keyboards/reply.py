from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# главное меню (каталог и помощь)
reply_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📂 Каталог"), 
     KeyboardButton(text="ℹ️ Помощь")]], resize_keyboard=True)