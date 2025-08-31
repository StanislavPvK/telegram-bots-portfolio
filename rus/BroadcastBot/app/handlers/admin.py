from aiogram import Bot, Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.services.broadcast import broadcast_message
from app.config import ADMIN_ID

admin_router = Router()


class BroadcastStates(StatesGroup):
    waiting_for_text = State()    # состояние ожидания текста для рассылки
    

# Клавиатура подтверждения или отмены рассылки
inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Подтвердить", callback_data="confirm_broadcast"),
    InlineKeyboardButton(text="❌ Отменить", callback_data="cancel_broadcast")]
])


@admin_router.message(Command("broadcast"))
async def cmd_broadcast(message: types.Message, state: FSMContext):
    
    # Проверка прав администратора
    if message.from_user.id != ADMIN_ID:
        return await message.answer("У вас нет прав для рассылки.")
    
    # Переходим в состояние ожидания текста
    await state.set_state(BroadcastStates.waiting_for_text)
    await message.answer("Введите текст для рассылки:")


@admin_router.message(BroadcastStates.waiting_for_text)
async def broadcast_text(message: types.Message, state: FSMContext):

    # Сохраняем введённый текст в состоянии
    await state.update_data(text=message.text)
    # Отправляем текст с кнопками подтверждения/отмены
    await message.answer(f"Вы ввели текст:\n\n{message.text}", reply_markup=inline_kb)


@admin_router.callback_query(F.data == "confirm_broadcast")
async def confirm_broadcast(callback: types.CallbackQuery, state: FSMContext, bot: Bot):

    # Получаем текст из состояния
    data = await state.get_data()
    text = data.get("text")

    if not text:
        await callback.message.answer("❌ Текст для рассылки не найден. Сначала введите сообщение.")
        await callback.answer()
        return

    # Отправка рассылки всем пользователям
    await broadcast_message(text, bot)

    # Очистка состояния после рассылки
    await state.clear()
    await callback.answer("Рассылка подтверждена ✅")
    await callback.message.edit_reply_markup(None)
    await callback.message.answer("Рассылка завершена")


@admin_router.callback_query(F.data == "cancel_broadcast")
async def cancel_broadcast(callback: types.CallbackQuery, state: FSMContext):

    # Отмена рассылки и очистка состояния
    await state.clear()
    await callback.answer("Рассылка отменена ❌")
    await callback.message.edit_reply_markup(None)
    await callback.message.answer("Рассылка отменена")