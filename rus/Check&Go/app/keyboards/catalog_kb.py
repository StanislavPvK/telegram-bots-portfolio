from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# инлайн-клавиатура с товарами
catalog_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📘 Чек-лист продуктивности — 9.9$", callback_data="productivity")],
    [InlineKeyboardButton(text="📙 Чек-лист по питанию — 14.9$", callback_data="nutrition")],
    [InlineKeyboardButton(text="📗 Чек-лист по планированию дня — 19.9$", callback_data="planning")]
])