from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from app.database import add_task, can_add_task
from app.keyboards.reply_kb import reply_kb

# Роутер для добавления задач
add_task_router = Router()


class AddTaskStates(StatesGroup):
    """FSM состояния для добавления новой задачи."""
    waiting_for_task = State()


@add_task_router.message(F.text == "Добавить задачу ✍️")
async def add_task_text(message: types.Message, state: FSMContext):
    """
    Обработчик команды "Добавить задачу".
    Проверяет, можно ли добавить новую задачу, и переводит пользователя
    в состояние ожидания ввода текста задачи.
    """

    # Проверяем, не превышен ли лимит задач
    if not await can_add_task(message.from_user.id):
        await message.answer("❌ Вы достигли лимита задач (4). Удалите старые задачи, чтобы добавить новые.")
        return
    
    # Устанавливаем состояние ожидания текста задачи
    await state.set_state(AddTaskStates.waiting_for_task)
    await message.answer("Введите текст задачи (до 150 символов):", reply_markup=ReplyKeyboardRemove())


@add_task_router.message(AddTaskStates.waiting_for_task)
async def save_task(message: types.Message, state: FSMContext):
    """
    Сохраняет новую задачу после ввода пользователем текста.
    Проверяет длину текста и обновляет базу данных.
    """

    task_text = message.text.strip()
    
    # Проверка длины текста
    if len(task_text) > 150:
        await message.answer("❌ Задача слишком длинная! Максимум 150 символов.", reply_markup=reply_kb)
        return
    
    # Сохраняем задачу в базе данных
    await add_task(message.from_user.id, task_text)
    await message.answer("✅ Задача добавлена!", reply_markup=reply_kb)

    # Сбрасываем состояние FSM
    await state.clear()