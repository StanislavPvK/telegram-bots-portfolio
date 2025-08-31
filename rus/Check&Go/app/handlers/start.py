from aiogram import Router, types
from aiogram.filters import CommandStart

from app.keyboards.reply import reply_kb

# Создаём роутер для команды /start
start_router = Router()


# обработка /start + показ клавиатуры
@start_router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет 👋\nЯ мини-магазин полезных чек-листов.\nВыбирай любой материал и получай сразу после оплаты!",
        reply_markup=reply_kb
    )