import sqlite3
conn = sqlite3.connect('example.db')

create_users_table = '''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL UNIQUE
);'''

c = conn.cursor()

c.execute(create_users_table)