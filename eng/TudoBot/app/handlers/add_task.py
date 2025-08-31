from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from app.database import add_task, can_add_task
from app.keyboards.reply_kb import reply_kb

# Router for adding tasks
add_task_router = Router()


class AddTaskStates(StatesGroup):
    """FSM states for adding a new task."""
    waiting_for_task = State()


@add_task_router.message(F.text == "Add Task ✍️")
async def add_task_text(message: types.Message, state: FSMContext):
    """
    Handler for the "Add Task" command.
    Checks if a new task can be added and sets the user
    to the state of waiting for task input.
    """

    # Check if the task limit is reached
    if not await can_add_task(message.from_user.id):
        await message.answer("❌ You have reached the task limit (4). Delete old tasks to add new ones.")
        return
    
    # Set the state to waiting for task text
    await state.set_state(AddTaskStates.waiting_for_task)
    await message.answer("Enter the task text (up to 150 characters):", reply_markup=ReplyKeyboardRemove())


@add_task_router.message(AddTaskStates.waiting_for_task)
async def save_task(message: types.Message, state: FSMContext):
    """
    Saves the new task after the user inputs the text.
    Checks the text length and updates the database.
    """

    task_text = message.text.strip()
    
    # Check text length
    if len(task_text) > 150:
        await message.answer("❌ Task is too long! Maximum 150 characters.", reply_markup=reply_kb)
        return
    
    # Save the task in the database
    await add_task(message.from_user.id, task_text)
    await message.answer("✅ Task added!", reply_markup=reply_kb)

    # Clear the FSM state
    await state.clear()
