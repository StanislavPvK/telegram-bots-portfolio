from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Клавиатура выбора категории
ctg_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Python 🐍", callback_data="ctg_python"),
     InlineKeyboardButton(text="История 📜", callback_data="ctg_history")]
])


# Генерация клавиатуры с вариантами ответа на вопрос
def get_question_keyboard(question_data: dict):
    buttons = []
    for i, option in enumerate(question_data["options"]):
        buttons.append([
            InlineKeyboardButton(
                text=option,
                callback_data=str(i)
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


# Клавиатура для повторного прохождения квиза
repeat_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пройти снова 🔄", callback_data="repeat_quiz")]
    ]
)