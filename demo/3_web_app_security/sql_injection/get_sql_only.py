import sqlite3

db_name = 'main.db'
conn = sqlite3.connect(db_name)

cur = conn.cursor()

cur.execute("SELECT * FROM user WHERE name='taro'")

print(cur.fetchall())

conn.close()