from aiogram import Router
from aiogram.types import CallbackQuery

from app.config import SUPPORTED_CRYPTOS
from app.keyboards.update_kb import update_kb
from app.services.crypto_api import get_crypto_price


# Router for handling cryptocurrency selection
price_router = Router()


@price_router.callback_query(lambda c: c.data in SUPPORTED_CRYPTOS)
async def handle_crypto_callback(callback: CallbackQuery):

    # Get the selected cryptocurrency
    crypto = callback.data

    # Request the current price
    price = await get_crypto_price(crypto)

    if price is not None:
        text = f"💰 {crypto.upper()} is currently {price} USD"
    else:
        # Error fetching the price
        text = "⚠️ Error fetching the price. Please try again later."

    await callback.message.answer(
        text=text,
        # Price refresh button
        reply_markup=update_kb(crypto)
    )

    await callback.answer()


# Handle the "Refresh" button
@price_router.callback_query(lambda c: c.data.startswith("update_"))
async def handle_update_callback(callback: CallbackQuery):
    
    # Extract the cryptocurrency from the callback
    crypto = callback.data.replace("update_", "")
    
    # Check if the currency is supported
    if crypto not in SUPPORTED_CRYPTOS:
        await callback.answer("Error: unknown currency", show_alert=True)
        return

    # Get the current price
    price = await get_crypto_price(crypto)

    if price is not None:
        text = f"💰 {crypto.upper()} is currently {price} USD"
    else:
        # Error fetching the price
        text = "⚠️ Error fetching the price. Please try again later."

    # Update the message if the price has changed
    if callback.message.text != text:
        await callback.message.edit_text(text=text, reply_markup=update_kb(crypto))
    else:
        # Notify without editing
        await callback.answer("Price is already updated ✅", show_alert=False)
