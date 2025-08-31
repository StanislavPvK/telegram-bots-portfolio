from aiogram import Router
from aiogram.types import CallbackQuery

from app.config import SUPPORTED_CRYPTOS
from app.keyboards.update_kb import update_kb
from app.services.crypto_api import get_crypto_price


# Роутер для обработки выбора криптовалюты
price_router = Router()


@price_router.callback_query(lambda c: c.data in SUPPORTED_CRYPTOS)
async def handle_crypto_callback(callback: CallbackQuery):

    # Получаем выбранную криптовалюту
    crypto = callback.data

    # Запрашиваем текущую цену
    price = await get_crypto_price(crypto)

    if price is not None:
        text = f"💰 {crypto.upper()} сейчас стоит {price} USD"
    else:
        # Ошибка при получении курса
        text = "⚠️ Ошибка при получении курса. Попробуйте позже."

    await callback.message.answer(
        text=text,
        # Кнопка обновления цены
        reply_markup=update_kb(crypto)
    )

    await callback.answer()


# Обработка кнопки обновить
@price_router.callback_query(lambda c: c.data.startswith("update_"))
async def handle_update_callback(callback: CallbackQuery):
    
    # Извлекаем криптовалюту из callback
    crypto = callback.data.replace("update_", "")
    
    # Проверка на поддержку валюты
    if crypto not in SUPPORTED_CRYPTOS:
        await callback.answer("Ошибка: неизвестная валюта", show_alert=True)
        return

    # Получаем актуальную цену
    price = await get_crypto_price(crypto)

    if price is not None:
        text = f"💰 {crypto.upper()} сейчас стоит {price} USD"
    else:
        # Ошибка получения курса
        text = "⚠️ Ошибка при получении курса. Попробуйте позже."

    # Обновляем сообщение, если изменился курс
    if callback.message.text != text:
        await callback.message.edit_text(text=text, reply_markup=update_kb(crypto))
    else:
        # Уведомление без редактирования
        await callback.answer("Курс уже обновлён ✅", show_alert=False)

