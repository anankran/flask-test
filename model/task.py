import psycopg2
import datetime

class Task:

  def list(self):
    conn = psycopg2.connect(
      host='ec2-23-23-177-166.compute-1.amazonaws.com',
      database='d6m14jp1b2sism',
      user='ocydywlrntdzjq',
      password='ffaa29344211f693a75f283720dba27b3811b5807167cbdc017cef946f4c01b5')
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
    conn = psycopg2.connect(
      host='ec2-23-23-177-166.compute-1.amazonaws.com',
      database='d6m14jp1b2sism',
      user='ocydywlrntdzjq',
      password='ffaa29344211f693a75f283720dba27b3811b5807167cbdc017cef946f4c01b5')
    cur = conn.cursor()
    date = datetime.datetime.now()

    sql = """
    INSERT INTO task (name, description, created_at, updated_at)
    VALUES (%s, %s, %s, %s)
    """
    response = cur.execute(sql, (form['name'], form['description'], date, date))
    id = cur.lastrowid
    conn.commit()
    conn.close()

    return id

  def done(self, id):
    conn = psycopg2.connect(
      host='ec2-23-23-177-166.compute-1.amazonaws.com',
      database='d6m14jp1b2sism',
      user='ocydywlrntdzjq',
      password='ffaa29344211f693a75f283720dba27b3811b5807167cbdc017cef946f4c01b5')
    cur = conn.cursor()
    status = 1

    cur.execute("""
    UPDATE task
    SET status = %s
    WHERE id = %s
    """, (status, id))
    conn.commit()
    conn.close()

    return id

