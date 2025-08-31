import aiosqlite

DB_NAME = "tasks.db"



async def init_db():
    """
    Инициализирует базу данных и создаёт таблицу tasks, если её нет.
    Таблица содержит:
        id       - уникальный идентификатор задачи
        user_id  - идентификатор пользователя
        task     - текст задачи
        status   - статус задачи (например, '❌' или '✅')
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
    Проверяет, можно ли добавить новую задачу для пользователя.
    Возвращает True, если текущий счёт задач меньше MAX_TASKS.
    """
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT COUNT(*) FROM tasks WHERE user_id = ?", (user_id,))
        result = await cursor.fetchone()
        task_count = result[0]

    return task_count < MAX_TASKS


async def add_task(user_id: int, task: str):
    """Добавляет новую задачу для пользователя с начальным статусом '❌'."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO tasks (user_id, task, status) VALUES (?, ?, ?)", 
            (user_id, task, "❌"))
        await db.commit()


async def get_tasks(user_id: int):
    """Возвращает список задач пользователя в формате (id, task, status)."""
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT id, task, status FROM tasks WHERE user_id = ?", 
            (user_id,))
        rows = await cursor.fetchall()
        return rows


async def update_status(task_id: int, new_status: str):
    """Обновляет статус задачи по её id."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE tasks SET status = ? WHERE id = ?",
            (new_status, task_id))
        await db.commit()
        

async def delete_task(task_id: int):
    """Удаляет задачу по её id."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,))
        await db.commit()