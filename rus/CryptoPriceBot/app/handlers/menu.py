from aiogram import Router, types
from aiogram.filters import Command

from app.keyboards.menu_kb import menu_kb


# Роутер для команды меню
menu_router = Router()


@menu_router.message(Command("menu"))
async def cmd_menu(message: types.Message):
    # Отправка клавиатуры выбора валюты
    await message.answer("Выберите валюту:", reply_markup=menu_kb)