import sqlite3
import datetime

class Task:

  def list(self):
    conn = sqlite3.connect('tasks_app.db')
    cur = conn.cursor()

    cur.execute("""
    SELECT * 
    FROM task 
    ORDER BY id DESC
    """)
    response = cur.fetchall()
    conn.close()

    return response

  def create(self, form):
    conn = sqlite3.connect('tasks_app.db')
    cur = conn.cursor()
    date = datetime.datetime.now()

    sql = """
    INSERT INTO task (name, description, created_at, updated_at)
    VALUES (?, ?, ?, ?)
    """
    response = cur.execute(sql, (form['name'], form['description'], date, date))
    id = cur.lastrowid
    conn.commit()
    conn.close()

    return id

  def done(self, id):
    conn = sqlite3.connect('tasks_app.db')
    cur = conn.cursor()
    status = 1

    cur.execute("""
    UPDATE task
    SET status = ?
    WHERE id = ?
    """, (status, id))
    conn.commit()
    conn.close()

    return id

