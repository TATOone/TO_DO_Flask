import psycopg2

conn = psycopg2.connect(
    dbname='flask_todo',
    user='tim',
    password='4200',
    host='localhost',
    port='5432'
)

def init_db():
    global conn
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT FALSE
    )
    ''')
    conn.commit()

def get_all_tasks():
    global conn
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, completed FROM tasks')
    rows = cursor.fetchall()
    return [{'id': row[0], 'title': row[1], 'completed': row[2]} for row in rows]

def add_task(title):
    global conn
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, completed) VALUES (%s, %s)', (title, False))
    conn.commit()
    return cursor.lastrowid

def update_task(task_id: int, title: str=None, completed: bool=None):
    global conn
    cursor = conn.cursor()
    if title is not None:
        cursor.execute('UPDATE tasks SET title=%s WHERE id=%s', (title, task_id))
    if completed is not None:
        cursor.execute('UPDATE tasks SET completed=%s WHERE id=%s', (completed, task_id))
    conn.commit()

def delete_task(task_id: int):
    global conn
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id=%s', (task_id,))

def get_task(task_id: int):
    global conn
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, completed FROM tasks WHERE id=%s', (task_id,))
    row = cursor.fetchone()
    return {'id': row[0], 'title': row[1], 'completed': row[2]}

if __name__ == '__main__':
    init_db()
    add_task('Learn psycopg2')
    print(get_all_tasks())