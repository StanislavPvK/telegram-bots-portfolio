from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Основная inline-клавиатура с кнопками "Выполнить" и "Удалить" для демонстрации
inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Выполнить задачу", callback_data="choose_done"),
    InlineKeyboardButton(text="❌ Удалить задачу", callback_data="choose_del")]
])


def create_tasks_keyboard(tasks: list[tuple[int, str, str]]):
    """
    Создаёт inline-клавиатуру с кнопками для выполнения задач.
    Включает только задачи со статусом отличным от '✅'.
    
    Args:
        tasks: Список кортежей задач в формате (id, текст, статус)
        
    Returns:
        InlineKeyboardMarkup с кнопками для выполнения задач
    """
    keyboard_buttons = []

    for task_id, task_text, status in tasks:
        if status != "✅":
            keyboard_buttons.append([InlineKeyboardButton(
                text=task_text,
                callback_data=f"done_{task_id}"
            )])

    return InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)


def tasks_kb_del(tasks: list[tuple[int, str, str]]):
    """
    Создаёт inline-клавиатуру с кнопками для удаления всех задач.
    
    Args:
        tasks: Список кортежей задач в формате (id, текст, статус)
        
    Returns:
        InlineKeyboardMarkup с кнопками для удаления задач
    """
    keyboard_buttons = []

    for task_id, task_text, _ in tasks:
        keyboard_buttons.append([InlineKeyboardButton(
        text=task_text,
        callback_data=f"del_{task_id}"
        )])

    return InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)