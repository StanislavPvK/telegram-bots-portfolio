import os
import aiosqlite


# Define project directory and folder for storing data
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))

DATA_DIR = os.path.join(root_dir, "data")
# Create data folder if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)


# Path to SQLite database
DB_NAME = os.path.join(DATA_DIR, "users_bcb.db")


# Initialize database and create users table
async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY            
        )
    """)
        await db.commit()


# Add a user (ignore if already exists)
async def add_user(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
            (user_id,))
        await db.commit()


# Get a list of all user_ids from the database
async def get_all_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT user_id FROM users"
        )
        rows = await cursor.fetchall()
        user_ids = [row[0] for row in rows]
        return user_ids
    

# Delete a user by user_id
async def delete_user(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "DELETE FROM users WHERE user_id = ?", (user_id,))
        await db.commit()
