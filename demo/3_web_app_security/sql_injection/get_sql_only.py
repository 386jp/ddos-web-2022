import sqlite3

def main():
    db_name = 'main.db'
    conn = sqlite3.connect(db_name)

    cur = conn.cursor()

    cur.execute("SELECT * FROM user WHERE name='taro'")

    print(cur.fetchall())

    conn.close()

if __name__ == '__main__':
    main()