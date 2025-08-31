from aiogram import F, Router
from aiogram.types import CallbackQuery, LabeledPrice, FSInputFile, Message
from aiogram.types.pre_checkout_query import PreCheckoutQuery

from app import config
from app.payments import get_product


# роутер для обработки покупок
purchase_router = Router()


@purchase_router.callback_query(lambda c: c.data and c.data.startswith("buy:"))

# обработка кнопки "Купить"
async def buy_product(callback: CallbackQuery):
    product_id = callback.data.split(":")[1]
    product = get_product(product_id)

    if not product:
        await callback.answer("Товар не найден", show_alert=True)
        return


    prices = [LabeledPrice(label=product.title, amount=product.price)]

    # отправка инвойса для оплаты
    await callback.message.answer_invoice(
        title=product.title,
        description=f"Купить {product.title}",
        payload=product.id,
        provider_token=config.PAYMENT_PROVIDER_TOKEN,
        currency="USD",
        prices=prices,
        start_parameter="purchase",
    )


# подтверждение предварительной оплаты
@purchase_router.pre_checkout_query()
async def pre_checkout(pre_checkout_q: PreCheckoutQuery):
    
    await pre_checkout_q.answer(ok=True)


# отправка файла после успешной оплаты
@purchase_router.message(F.successful_payment)
async def successful_payment(message: Message):
    product_id = message.successful_payment.invoice_payload
    product = get_product(product_id)

    if not product:
        await message.answer("Что-то пошло не так...")
        return

    file = FSInputFile(product.file_path)

    await message.answer_document(
        file, caption=f"✅ Спасибо за покупку! Вот ваш файл: {product.title}"
    )