import sqlite3

db_name = 'main.db'
conn = sqlite3.connect(db_name)

cur = conn.cursor()

cur.execute(
    'CREATE TABLE user(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING, gender STRING, age INTEGER)'
)

inserts = [
    (1, "Kyosuke Miyamura", "MALE", 21),
    (2, "Hoge Fuga", "FEMALE", 30),
    (3, "John Cena", "MALE", 44),
    (4, "taro", "MALE", 12)
]

cur.executemany('INSERT INTO user values(?, ?, ?, ?)', inserts)

conn.commit()

conn.close()