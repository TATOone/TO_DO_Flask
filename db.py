import sqlite3

DB_name = 'tasks.db'

def init_db():
    with (sqlite3.connect(DB_name) as conn):
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
            )
        ''')
        conn.commit()

def get_all_tasks():
    with sqlite3.connect(DB_name) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, completed FROM tasks')
        rows = cursor.fetchall()
        return [{'id': row[0], 'title': row[1], 'completed': row[2]} for row in rows]

def add_task(title):
    with sqlite3.connect(DB_name) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (title, False))
        conn.commit()
        return cursor.lastrowid

def update_task(task_id: int, title: str=None, completed: bool=None):
    with sqlite3.connect(DB_name) as conn:
        cursor = conn.cursor()
        if title is not None:
            cursor.execute('UPDATE tasks SET title=? WHERE id=?', (title, task_id))
        if completed is not None:
            cursor.execute('UPDATE tasks SET completed=? WHERE id=?', (completed, task_id))
        conn.commit()

def delete_task(task_id: int):
    with sqlite3.connect(DB_name) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))

def get_task(task_id: int):
    with sqlite3.connect(DB_name) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, completed FROM tasks WHERE id=?', (task_id,))
        row = cursor.fetchone()
        return {'id': row[0], 'title': row[1], 'completed': row[2]}
