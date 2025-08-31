from aiogram import Router, types
from aiogram.filters import CommandStart

from app.keyboards.reply import reply_kb

# Create router for the /start command
start_router = Router()


# Handle /start command and show main keyboard
@start_router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Hello 👋\nI am a mini-store for useful checklists.\nChoose any material and get it immediately after payment!",
        reply_markup=reply_kb
    )
