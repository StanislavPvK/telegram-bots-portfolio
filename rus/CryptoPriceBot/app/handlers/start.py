from aiogram import Router, types
from aiogram.filters import CommandStart


# Роутер для команды старт
start_router = Router()


# Отправка приветственного сообщения пользователю
@start_router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот для просмотра курса криптовалют.\n" \
        "Используй /menu, чтобы выбрать валюту.", 
    )