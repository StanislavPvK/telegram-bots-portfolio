from aiogram import Router, types
from aiogram.filters import CommandStart

from app.keyboards.reply_kb import reply_kb

# Создаём роутер для команды /start
start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: types.Message):
    """
    Обработчик команды /start.
    Отправляет приветственное сообщение пользователю
    и показывает основную клавиатуру с выбором действий.
    """
    await message.answer(
        "Привет! ✨\nЯ TodoBot.\nВыберите: «Добавить задачу» или «Список задач».", 
        reply_markup=reply_kb)