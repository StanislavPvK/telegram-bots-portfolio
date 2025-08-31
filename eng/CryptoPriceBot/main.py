import logging
import asyncio
from aiogram import Dispatcher, Bot

from app import config
from app.handlers.start import start_router
from app.handlers.menu import menu_router
from app.handlers.price import price_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")


async def main():
    """
    Main function to run the bot:
    - creates Bot and Dispatcher objects
    - includes bot routers
    - initializes the database
    - starts polling
    """

    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()

    # Include bot handlers (routers)
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(price_router)

    # Remove previous webhook and drop pending updates
    await bot.delete_webhook(drop_pending_updates=True)
    logging.info("Bot started. Polling...")
    
    # Run the bot and start polling
    try:
        await dp.start_polling(bot)
    finally:
        # Close the bot session when finished
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped")
