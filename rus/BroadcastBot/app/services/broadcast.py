import asyncio
from aiogram.exceptions import TelegramForbiddenError

from app.database import db


async def broadcast_message(text, bot):

    # Получаем список всех зарегистрированных пользователей
    user_ids = await db.get_all_users()
    for user_id in user_ids:
        try:
            # Отправка сообщения пользователю
            await bot.send_message(user_id, text)

        except TelegramForbiddenError as e:
            
            # Если бот заблокирован или чат не найден, удаляем пользователя из базы
            if "bot was blocked by the user" in str(e) or "chat not found" in str(e):
                print(f"Пользователь {user_id} заблокировал бота или удалил аккаунт")
                await db.delete_user(user_id)
                
            else:
                print(f"Ошибка при отправке {user_id}: {e}")

        # Ловим все неожиданные ошибки
        except Exception as e:
            print(f"Неожиданная ошибка при отправке {user_id}: {e}")

        # Небольшая пауза между отправками, чтобы избежать ограничения Telegram
        await asyncio.sleep(0.3)

