from db import get_db_connection

def get_all_tasks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM todo")
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records

def add_task(task: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todo (task) VALUES (%s)", (task,))
    conn.commit()
    cursor.close()
    conn.close()

def delete_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todo WHERE id = %s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
