import asyncio
import logging
from aiogram import Bot, Dispatcher

from app import config
from app.database import db
from app.handlers.user import user_router
from app.handlers.admin import admin_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")


async def main():
    """
    Main bot startup function:
    - creates Bot and Dispatcher objects
    - connects routers
    - initializes the database
    - starts polling
    """

    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()
    
    await db.init_db()

    # Connect bot handlers (routers)
    dp.include_router(user_router)
    dp.include_router(admin_router)

    # Remove previous webhook and drop pending updates
    await bot.delete_webhook(drop_pending_updates=True)
    logging.info("Bot started. Polling...")
    # Run the bot and start polling
    try:
        await dp.start_polling(bot)
    finally:
        # Close the bot session on shutdown
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped")
