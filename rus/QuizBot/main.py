import asyncio
import logging
from aiogram import Bot, Dispatcher

from app import config
from app.handlers.start import start_router
from app.handlers.quiz import quiz_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")


async def main():
    """
    Главная функция запуска бота:
    - создаёт объект Bot и Dispatcher
    - подключает маршруты (routers)
    - инициализирует базу данных
    - запускает polling
    """

    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()

    # Подключаем хендлеры (маршруты) бота
    dp.include_router(start_router)
    dp.include_router(quiz_router)


    # Удаляем предыдущий вебхук и сбрасываем ожидающие обновления
    await bot.delete_webhook(drop_pending_updates=True)
    logging.info("Бот запущен. Polling...")
    # Запускаем бота и начинаем polling
    try:
        await dp.start_polling(bot)
    finally:
        # Закрываем сессию бота при завершении работы
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен")