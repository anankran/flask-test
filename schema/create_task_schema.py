import sqlite3

conn = sqlite3.connect('tasks_app.db')
cur = conn.cursor()

cur.execute("""
DROP TABLE IF EXISTS task
""")

cur.execute("""
CREATE TABLE task (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        status INTEGER DEFAULT 0,
        created_at DATETIME,
        updated_at DATETIME
);
""")

conn.commit()
conn.close()