from aiogram import Router, types
from aiogram.filters import CommandStart

from app.keyboards.inline import ctg_inline_kb


# Создаём роутер для команды /start
start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: types.Message):
    """
    Обработчик команды /start.
    Отправляет приветственное сообщение пользователю
    и показывает клавиатуру с выбором категории.
    """
    await message.answer(
         "Привет! 👋\n"
        "*QuizBot* поможет тебе проверить знания в разных категориях.\n\n"
        "Выбери категорию, чтобы начать викторину:", 
        reply_markup=ctg_inline_kb, parse_mode="Markdown")