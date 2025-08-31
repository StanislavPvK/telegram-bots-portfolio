from aiogram import Router, types
from aiogram.filters import CommandStart

from app.keyboards.inline import ctg_inline_kb


# Create a router for the /start command
start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: types.Message):
    """
    Handler for the /start command.
    Sends a welcome message to the user
    and shows the keyboard for category selection.
    """
    await message.answer(
         "Hello! 👋\n"
        "*QuizBot* will help you test your knowledge in different categories.\n\n"
        "Choose a category to start the quiz:", 
        reply_markup=ctg_inline_kb, parse_mode="Markdown")
