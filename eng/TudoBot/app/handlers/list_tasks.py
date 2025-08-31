from aiogram import Router, F, types

from app.database import get_tasks
from app.keyboards.inline_kb import inline_kb


# Create a router to handle the "Task List" command
list_tasks_router = Router()


@list_tasks_router.message(F.text == ("Task List 📜"))
async def list_tasks(message: types.Message):
    """
    Handler for the "Task List 📜" message.
    Retrieves all user tasks from the database and sends them
    with an inline keyboard for task actions.
    """

    # Get all user tasks from the database
    tasks = await get_tasks(message.from_user.id)
   
    # If there are no tasks — inform the user
    if not tasks:
        await message.answer("📭 You currently have no tasks.")
        return
    
    # Form a text message with the list of tasks
    text = "📝 Your tasks:\n\n" + "\n".join(
        f"• {task_text} — {status}" 
        for _, task_text, status in tasks
    )

    # Send the message with an inline keyboard for task management
    await message.answer(text, reply_markup=inline_kb)
