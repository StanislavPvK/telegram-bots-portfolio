from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Inline keyboard with products
catalog_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📘 Productivity Checklist — $9.9", callback_data="productivity")],
    [InlineKeyboardButton(text="📙 Nutrition Checklist — $14.9", callback_data="nutrition")],
    [InlineKeyboardButton(text="📗 Daily Planning Checklist — $19.9", callback_data="planning")]
])
