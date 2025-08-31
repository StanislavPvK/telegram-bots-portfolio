import aiosqlite

DB_NAME = "tasks.db"


async def init_db():
    """
    Initializes the database and creates the tasks table if it doesn't exist.
    The table contains:
        id       - unique task identifier
        user_id  - user identifier
        task     - task text
        status   - task status (e.g., '❌' or '✅')
    """
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            task TEXT,
            status TEXT          
        )
    """)
        await db.commit()


MAX_TASKS = 4


async def can_add_task(user_id: int):
    """
    Checks if a new task can be added for the user.
    Returns True if the current number of tasks is less than MAX_TASKS.
    """
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT COUNT(*) FROM tasks WHERE user_id = ?", (user_id,))
        result = await cursor.fetchone()
        task_count = result[0]

    return task_count < MAX_TASKS


async def add_task(user_id: int, task: str):
    """Adds a new task for the user with the initial status '❌'."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO tasks (user_id, task, status) VALUES (?, ?, ?)", 
            (user_id, task, "❌"))
        await db.commit()


async def get_tasks(user_id: int):
    """Returns a list of the user's tasks in the format (id, task, status)."""
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT id, task, status FROM tasks WHERE user_id = ?", 
            (user_id,))
        rows = await cursor.fetchall()
        return rows


async def update_status(task_id: int, new_status: str):
    """Updates the status of a task by its id."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE tasks SET status = ? WHERE id = ?",
            (new_status, task_id))
        await db.commit()
        

async def delete_task(task_id: int):
    """Deletes a task by its id."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,))
        await db.commit()
