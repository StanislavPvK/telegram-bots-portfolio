import asyncio
from aiogram.exceptions import TelegramForbiddenError

from app.database import db


async def broadcast_message(text, bot):

    # Get the list of all registered users
    user_ids = await db.get_all_users()
    for user_id in user_ids:
        try:
            # Send message to the user
            await bot.send_message(user_id, text)

        except TelegramForbiddenError as e:
            
            # If the bot is blocked or chat not found, remove the user from the database
            if "bot was blocked by the user" in str(e) or "chat not found" in str(e):
                print(f"User {user_id} blocked the bot or deleted the account")
                await db.delete_user(user_id)
                
            else:
                print(f"Error sending to {user_id}: {e}")

        # Catch all unexpected errors
        except Exception as e:
            print(f"Unexpected error sending to {user_id}: {e}")

        # Small pause between sends to avoid Telegram rate limits
        await asyncio.sleep(0.3)

