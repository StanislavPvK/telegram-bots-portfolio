from aiogram import Router, F, types


# роутер для обработки кнопки "Помощь"
help_router = Router()


# обработка нажатия кнопки помощи
@help_router.message(F.text == "ℹ️ Помощь")
async def btn_help(message: types.Message):
    await message.answer(
        "Я бот-магазин цифровых чек-листов 📚\n" \
        "Все материалы доступны сразу после оплаты.\n" \
        "Если есть вопросы — напиши в поддержку: @username")