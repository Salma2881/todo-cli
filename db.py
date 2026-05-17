import sqlite3
import os
DB_PATH = os.path.join(os.path.dirname(__file__), "todos.db")
def get_connection():
    return sqlite3.connect(DB_PATH) 
def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                task       TEXT    NOT NULL,
                done       INTEGER NOT NULL DEFAULT 0,
                created_at TEXT    NOT NULL DEFAULT (datetime('now'))
            )
        """)
        conn.commit()
def add_task(task: str) -> int:
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO todos (task) VALUES (?)", (task,)
        )
        conn.commit()
        return cursor.lastrowid
def list_tasks(show_all: bool = False) -> list:
    with get_connection() as conn:
        conn.row_factory = sqlite3.Row
        if show_all:
            rows = conn.execute(
                "SELECT * FROM todos ORDER BY created_at"
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM todos WHERE done = 0 ORDER BY created_at"
            ).fetchall()
        return [dict(row) for row in rows]        
def mark_done(task_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE todos SET done = 1 WHERE id = ? AND done = 0", (task_id,)
        )
        conn.commit()
        return cursor.rowcount > 0


def delete_task(task_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM todos WHERE id = ?", (task_id,)
        )
        conn.commit()
        return cursor.rowcount > 0        