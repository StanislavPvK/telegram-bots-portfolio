from aiogram import Router, F, types

from app.keyboards.catalog_kb import catalog_kb
from app.keyboards.product_kb import product_detail_kb
from app.payments import get_product


# роутер для каталога товаров
catalog_router = Router()


# кнопка "Каталог"
@catalog_router.message(F.text == "📂 Каталог")
async def btn_catalog(message: types.Message):
    await message.answer(
        "📂 Наш каталог\n" \
        "Выберите интересующий вас чек-лист:", reply_markup=catalog_kb)
    

# кнопка "Назад" в деталях товара
@catalog_router.callback_query(F.data == "back_to_catalog")
async def back_to_catalog(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "📂 Наш каталог\nВыберите интересующий вас чек-лист:",
        reply_markup=catalog_kb
    )


# показ деталей товара при нажатии на инлайн-кнопку
@catalog_router.callback_query()
async def show_product_detail(callback: types.CallbackQuery):
    product_id = callback.data
    product = get_product(product_id)
    if not product:
        await callback.answer("Товар не найден")
        return
    
    text = f"📘 {product.title}\nЦена: {product.price / 100:.2f}$\n\n" \
        "Внутри: полезный чек-лист для повышения эффективности."
    
    await callback.message.edit_text(
        text=text,
        reply_markup=product_detail_kb(product_id)   # кнопки "Купить" и "Назад"
    )