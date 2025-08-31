from aiogram import Router, F, types

from app.keyboards.catalog_kb import catalog_kb
from app.keyboards.product_kb import product_detail_kb
from app.payments import get_product


# Router for the product catalog
catalog_router = Router()


# "Catalog" button
@catalog_router.message(F.text == "📂 Catalog")
async def btn_catalog(message: types.Message):
    await message.answer(
        "📂 Our Catalog\n" \
        "Select the checklist you are interested in:", reply_markup=catalog_kb)
    

# "Back" button in product details
@catalog_router.callback_query(F.data == "back_to_catalog")
async def back_to_catalog(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "📂 Our Catalog\nSelect the checklist you are interested in:",
        reply_markup=catalog_kb
    )


# Show product details when an inline button is pressed
@catalog_router.callback_query()
async def show_product_detail(callback: types.CallbackQuery):
    product_id = callback.data
    product = get_product(product_id)
    if not product:
        await callback.answer("Product not found")
        return
    
    text = f"📘 {product.title}\nPrice: {product.price / 100:.2f}$\n\n" \
        "Inside: a useful checklist to improve productivity."
    
    await callback.message.edit_text(
        text=text,
        reply_markup=product_detail_kb(product_id)   # "Buy" and "Back" buttons
    )
