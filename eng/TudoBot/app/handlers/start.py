from aiogram import Router, types
from aiogram.filters import CommandStart

from app.keyboards.reply_kb import reply_kb

# Create a router for the /start command
start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: types.Message):
    """
    Handler for the /start command.
    Sends a welcome message to the user
    and shows the main keyboard with action choices.
    """
    await message.answer(
        "Hello! ✨\nI'm TodoBot.\nChoose: 'Add Task' or 'Task List'.", 
        reply_markup=reply_kb)
