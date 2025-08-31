from aiogram import Router, F, types


# Router for handling the "Help" button
help_router = Router()


# Handle pressing the help button
@help_router.message(F.text == "ℹ️ Help")
async def btn_help(message: types.Message):
    await message.answer(
        "I am a digital checklist store bot 📚\n"
        "All materials are available immediately after payment.\n"
        "If you have any questions, contact support: @username"
    )
