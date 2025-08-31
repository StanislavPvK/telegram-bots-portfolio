from aiogram import Router, F, types

from app.database import get_tasks, update_status, delete_task
from app.keyboards.reply_kb import reply_kb
from app.keyboards.inline_kb import create_tasks_keyboard, tasks_kb_del


# Router for handling callback_query
callback_router = Router()


@callback_router.callback_query(F.data == "choose_done")
async def choose_task_to_done(callback: types.CallbackQuery):
    """
    Handler for pressing the "Complete Task" button.
    Shows the user a list of tasks that can be completed.
    """

    tasks = await get_tasks(callback.from_user.id)

    # If there are no tasks — inform the user
    if not tasks:
        await callback.message.answer("📭 You have no tasks to complete.", reply_markup=reply_kb)
        await callback.answer()
        return
    
    # Create a keyboard with tasks to complete
    tasks_keyboard = create_tasks_keyboard(tasks)

    await callback.message.answer("Select a task to complete:", reply_markup=tasks_keyboard)
    await callback.answer()


@callback_router.callback_query(F.data == "choose_del")
async def choose_task_to_delete(callback: types.CallbackQuery):
    """
    Handler for pressing the "Delete Task" button.
    Shows the user a list of tasks that can be deleted.
    """

    tasks = await get_tasks(callback.from_user.id)

    if not tasks:
        await callback.message.answer("📭 You have no tasks to delete.", reply_markup=reply_kb)
        await callback.answer()
        return

    # Create a keyboard with tasks to delete
    delete_tasks_keyboard = tasks_kb_del(tasks)

    await callback.message.answer("Select a task to delete:", reply_markup=delete_tasks_keyboard)
    await callback.answer()


@callback_router.callback_query(F.data.startswith("done_"))
async def complete_task(callback: types.CallbackQuery):
    """
    Handler for pressing the button to complete a specific task.
    Updates the task status in the database and notifies the user.
    """

    task_id = int(callback.data.split("_")[1])

    await update_status(task_id, "✅")
    await callback.message.answer("✅ Task marked as completed!", reply_markup=reply_kb)
    await callback.answer()


@callback_router.callback_query(F.data.startswith("del_"))
async def remove_task(callback: types.CallbackQuery):
    """
    Handler for pressing the button to delete a specific task.
    Deletes the task from the database and notifies the user.
    """

    task_id = int(callback.data.split("_")[1])

    await delete_task(task_id)
    await callback.message.answer("❌ Task deleted!", reply_markup=reply_kb)
    await callback.answer()
