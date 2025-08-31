from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Category selection keyboard
ctg_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Python 🐍", callback_data="ctg_python"),
     InlineKeyboardButton(text="History 📜", callback_data="ctg_history")]
])


# Generate a keyboard with answer options for a question
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


# Keyboard for retaking the quiz
repeat_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Take Again 🔄", callback_data="repeat_quiz")]
    ]
)
