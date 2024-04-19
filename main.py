import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS users
#     (id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER NOT NULL)
#     ''')
#
# conn.commit()
#
# cur.execute('INSERT INTO users(name, age) VALUES(?, ?)', ("Vasya", 20))
# cur.execute('INSERT INTO users(name, age) VALUES(?, ?)', ("Petya", 30))
#
# conn.commit()

cur.execute('SELECT * FROM users')
rows = cur.fetchall()
#print(rows) - Выводит весь список в одну строку

for row in rows:
    print(row)

conn.close()