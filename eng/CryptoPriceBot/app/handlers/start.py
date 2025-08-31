from aiogram import Router, types
from aiogram.filters import CommandStart


# Router for the /start command
start_router = Router()


# Send a welcome message to the user
@start_router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Hello! I am a bot for checking cryptocurrency prices.\n"
        "Use /menu to choose a currency.",
    )
