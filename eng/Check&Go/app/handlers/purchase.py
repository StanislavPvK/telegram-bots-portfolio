from aiogram import F, Router
from aiogram.types import CallbackQuery, LabeledPrice, FSInputFile, Message
from aiogram.types.pre_checkout_query import PreCheckoutQuery

from app import config
from app.payments import get_product


# Router for handling purchases
purchase_router = Router()


@purchase_router.callback_query(lambda c: c.data and c.data.startswith("buy:"))
# Handle the "Buy" button
async def buy_product(callback: CallbackQuery):
    product_id = callback.data.split(":")[1]
    product = get_product(product_id)

    if not product:
        await callback.answer("Product not found", show_alert=True)
        return

    prices = [LabeledPrice(label=product.title, amount=product.price)]

    # Send invoice for payment
    await callback.message.answer_invoice(
        title=product.title,
        description=f"Buy {product.title}",
        payload=product.id,
        provider_token=config.PAYMENT_PROVIDER_TOKEN,
        currency="USD",
        prices=prices,
        start_parameter="purchase",
    )


# Pre-checkout confirmation
@purchase_router.pre_checkout_query()
async def pre_checkout(pre_checkout_q: PreCheckoutQuery):
    await pre_checkout_q.answer(ok=True)


# Send the file after successful payment
@purchase_router.message(F.successful_payment)
async def successful_payment(message: Message):
    product_id = message.successful_payment.invoice_payload
    product = get_product(product_id)

    if not product:
        await message.answer("Something went wrong...")
        return

    file = FSInputFile(product.file_path)

    await message.answer_document(
        file, caption=f"✅ Thank you for your purchase! Here is your file: {product.title}"
    )
