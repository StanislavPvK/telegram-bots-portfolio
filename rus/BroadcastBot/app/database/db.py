import os
import aiosqlite


# Определяем директорию проекта и папку для хранения данных
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))

DATA_DIR = os.path.join(root_dir, "data")
# создаем папку data, если не существует
os.makedirs(DATA_DIR, exist_ok=True)


# Путь к базе данных SQLite
DB_NAME = os.path.join(DATA_DIR, "users_bcb.db")


# Инициализация базы данных и создание таблицы пользователей
async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY            
        )
    """)
        await db.commit()


# Добавление пользователя (игнорируем, если уже существует)
async def add_user(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
            (user_id,))
        await db.commit()


# Получение списка всех user_id из базы
async def get_all_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT user_id FROM users"
        )
        rows = await cursor.fetchall()
        user_ids = [row[0] for row in rows]
        return user_ids
    

# Удаление пользователя по user_id
async def delete_user(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "DELETE FROM users WHERE user_id = ?", (user_id,))
        await db.commit()