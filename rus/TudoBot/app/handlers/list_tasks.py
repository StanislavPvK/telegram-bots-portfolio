from aiogram import Router, F, types

from app.database import get_tasks
from app.keyboards.inline_kb import inline_kb


# Создаём роутер для обработки команды "Список задач"
list_tasks_router = Router()


@list_tasks_router.message(F.text == ("Список задач 📜"))
async def list_tasks(message: types.Message):
    """
    Обработчик сообщения "Список задач 📜".
    Получает все задачи пользователя из базы данных и отправляет их
    с inline-клавиатурой для действий с задачами.
    """

    # Получаем все задачи пользователя из базы данных
    tasks = await get_tasks(message.from_user.id)
   
    # Если задач нет — информируем пользователя
    if not tasks:
        await message.answer("📭 У вас пока нет задач.")
        return
    
    # Формируем текстовое сообщение со списком задач
    text = "📝 Ваши задачи:\n\n" + "\n".join(
    f"• {task_text} — {status}" 
    for _, task_text, status in tasks)

    # Отправляем сообщение с inline-клавиатурой для управления задачами
    await message.answer(text, reply_markup=inline_kb)