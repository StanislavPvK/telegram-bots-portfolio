from aiogram import Bot, Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.services.broadcast import broadcast_message
from app.config import ADMIN_ID

admin_router = Router()


class BroadcastStates(StatesGroup):
    waiting_for_text = State()    # state waiting for broadcast text
    

# Confirmation or cancellation keyboard
inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Confirm", callback_data="confirm_broadcast"),
     InlineKeyboardButton(text="❌ Cancel", callback_data="cancel_broadcast")]
])


@admin_router.message(Command("broadcast"))
async def cmd_broadcast(message: types.Message, state: FSMContext):
    
    # Check admin rights
    if message.from_user.id != ADMIN_ID:
        return await message.answer("You do not have permissions to broadcast.")
    
    # Move to state waiting for text
    await state.set_state(BroadcastStates.waiting_for_text)
    await message.answer("Enter the text for broadcasting:")


@admin_router.message(BroadcastStates.waiting_for_text)
async def broadcast_text(message: types.Message, state: FSMContext):

    # Save the entered text in the state
    await state.update_data(text=message.text)
    # Send text with confirmation/cancel buttons
    await message.answer(f"You entered the text:\n\n{message.text}", reply_markup=inline_kb)


@admin_router.callback_query(F.data == "confirm_broadcast")
async def confirm_broadcast(callback: types.CallbackQuery, state: FSMContext, bot: Bot):

    # Get text from state
    data = await state.get_data()
    text = data.get("text")

    if not text:
        await callback.message.answer("❌ Broadcast text not found. Please enter the message first.")
        await callback.answer()
        return

    # Send broadcast to all users
    await broadcast_message(text, bot)

    # Clear state after broadcasting
    await state.clear()
    await callback.answer("Broadcast confirmed ✅")
    await callback.message.edit_reply_markup(None)
    await callback.message.answer("Broadcast completed")


@admin_router.callback_query(F.data == "cancel_broadcast")
async def cancel_broadcast(callback: types.CallbackQuery, state: FSMContext):

    # Cancel broadcast and clear state
    await state.clear()
    await callback.answer("Broadcast cancelled ❌")
    await callback.message.edit_reply_markup(None)
    await callback.message.answer("Broadcast cancelled")