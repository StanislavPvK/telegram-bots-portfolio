from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Main inline keyboard with "Complete" and "Delete" buttons for demonstration
inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Complete Task", callback_data="choose_done"),
     InlineKeyboardButton(text="❌ Delete Task", callback_data="choose_del")]
])


def create_tasks_keyboard(tasks: list[tuple[int, str, str]]):
    """
    Creates an inline keyboard with buttons for completing tasks.
    Includes only tasks with a status different from '✅'.
    
    Args:
        tasks: List of task tuples in the format (id, text, status)
        
    Returns:
        InlineKeyboardMarkup with buttons for completing tasks
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
    Creates an inline keyboard with buttons to delete all tasks.
    
    Args:
        tasks: List of task tuples in the format (id, text, status)
        
    Returns:
        InlineKeyboardMarkup with buttons for deleting tasks
    """
    keyboard_buttons = []

    for task_id, task_text, _ in tasks:
        keyboard_buttons.append([InlineKeyboardButton(
            text=task_text,
            callback_data=f"del_{task_id}"
        )])

    return InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
