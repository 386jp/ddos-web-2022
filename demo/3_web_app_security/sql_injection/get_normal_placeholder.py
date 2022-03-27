import sqlite3

db_name = 'main.db'
conn = sqlite3.connect(db_name)

cur = conn.cursor()

name = "taro"

cur.execute(f"SELECT * FROM user WHERE name='{name}'")

print(cur.fetchall())

conn.close()