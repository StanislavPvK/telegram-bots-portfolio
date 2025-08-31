from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создаём клавиатуру с двумя кнопками для пользователя
reply_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Добавить задачу ✍️"), KeyboardButton(text="Список задач 📜")]
    ], resize_keyboard=True)