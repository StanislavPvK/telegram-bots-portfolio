from aiogram.filters import CommandStart
from aiogram import Router, types

from app.database.db import add_user
from app.config import ADMIN_ID


user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: types.Message):

    # Greeting when starting the bot
    if message.from_user.id == ADMIN_ID:
        # Message for the administrator
        await message.answer("Hello, admin! ⚡ Use /broadcast to send a broadcast.")
        return
    else:
        # Add new user to the database
        await add_user(message.from_user.id)
        await message.answer(f"Hello, {message.from_user.first_name}! You have been successfully registered and will receive notifications.")
 