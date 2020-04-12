import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute("SELECT * FROM users")

columns = c.description

print(columns)

[print(i) for i in c.fetchall()]