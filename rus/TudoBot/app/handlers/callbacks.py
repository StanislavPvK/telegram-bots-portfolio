from aiogram import Router, F, types

from app.database import get_tasks, update_status, delete_task
from app.keyboards.reply_kb import reply_kb
from app.keyboards.inline_kb import create_tasks_keyboard, tasks_kb_del


# Роутер для обработки callback_query
callback_router = Router()


@callback_router.callback_query(F.data == "choose_done")
async def choose_task_to_done(callback: types.CallbackQuery):
    """
    Обработчик нажатия кнопки "Выполнить задачу".
    Показывает пользователю список задач, которые можно выполнить.
    """

    tasks = await get_tasks(callback.from_user.id)

    # Если задач нет — информируем пользователя
    if not tasks:
        await callback.message.answer("📭 У вас нет задач для выполнения.", reply_markup=reply_kb)
        await callback.answer()
        return
    
    # Создаём клавиатуру с задачами для выполнения
    tasks_keyboard = create_tasks_keyboard(tasks)

    await callback.message.answer("Выберите задачу для выполнения:", reply_markup=tasks_keyboard)
    await callback.answer()


@callback_router.callback_query(F.data == "choose_del")
async def choose_task_to_delete(callback: types.CallbackQuery):
    """
    Обработчик нажатия кнопки "Удалить задачу".
    Показывает пользователю список задач для удаления.
    """

    tasks = await get_tasks(callback.from_user.id)

    if not tasks:
        await callback.message.answer("📭 У вас нет задач для удаления.", reply_markup=reply_kb)
        await callback.answer()
        return

    # Создаём клавиатуру с задачами для удаления
    delete_tasks_keyboard = tasks_kb_del(tasks)

    await callback.message.answer("Выберите задачу для удаления:", reply_markup=delete_tasks_keyboard)
    await callback.answer()


@callback_router.callback_query(F.data.startswith("done_"))
async def complete_task(callback: types.CallbackQuery):
    """
    Обработчик нажатия кнопки выполнения конкретной задачи.
    Обновляет статус задачи в базе данных и уведомляет пользователя.
    """

    task_id = int(callback.data.split("_")[1])

    await update_status(task_id, "✅")
    await callback.message.answer("✅ Задача отмечена как выполненная!", reply_markup=reply_kb)
    await callback.answer()


@callback_router.callback_query(F.data.startswith("del_"))
async def remove_task(callback: types.CallbackQuery):
    """
    Обработчик нажатия кнопки удаления конкретной задачи.
    Удаляет задачу из базы данных и уведомляет пользователя.
    """

    task_id = int(callback.data.split("_")[1])

    await delete_task(task_id)
    await callback.message.answer("❌ Задача удалена!", reply_markup=reply_kb)
    await callback.answer()