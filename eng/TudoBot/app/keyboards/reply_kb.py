from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Create a keyboard with two buttons for the user
reply_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Add Task ✍️"), KeyboardButton(text="Task List 📜")]
    ], resize_keyboard=True)
