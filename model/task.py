import psycopg2
import datetime

class Task:

  def list(self):
    conn = psycopg2.connect("dbname=d2nd6r6hbl7v0q user=yjyevrzvefzlsx")
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
    conn = psycopg2.connect("dbname=d2nd6r6hbl7v0q user=yjyevrzvefzlsx")
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
    conn = psycopg2.connect("dbname=d2nd6r6hbl7v0q user=yjyevrzvefzlsx")
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

