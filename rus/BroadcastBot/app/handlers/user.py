from aiogram.filters import CommandStart
from aiogram import Router, types

from app.database.db import add_user
from app.config import ADMIN_ID


user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: types.Message):

    # Приветствие при старте бота
    if message.from_user.id == ADMIN_ID:
        # Сообщение для администратора
        await message.answer("Привет, админ! ⚡ Используй /broadcast для рассылки.")
        return
    else:
        # Добавление нового пользователя в базу
        await add_user(message.from_user.id)
        await message.answer(f"Привет, {message.from_user.first_name}! Ты успешно зарегистрирован и будешь получать уведомления.") 