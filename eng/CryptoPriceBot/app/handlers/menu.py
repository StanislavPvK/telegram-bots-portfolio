from aiogram import Router, types
from aiogram.filters import Command

from app.keyboards.menu_kb import menu_kb


# Router for the menu command
menu_router = Router()


@menu_router.message(Command("menu"))
async def cmd_menu(message: types.Message):
    # Send the currency selection keyboard
    await message.answer("Choose a currency:", reply_markup=menu_kb)
