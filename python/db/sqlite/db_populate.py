import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute("INSERT INTO users (first_name, last_name, email, phone) VALUES ('Ivan','Ivanov','ivan@example.com','223-322')")
c.execute("INSERT INTO users (first_name, last_name, email, phone) VALUES ('Peter','Petrov','peter@example.com','243-322')")
c.execute("INSERT INTO users (first_name, last_name, email, phone) VALUES ('Sergei','Ivanov','sergei@example.com','253-322')")
c.execute("INSERT INTO users (first_name, last_name, email, phone) VALUES ('Igor','Ivanov','igor@example.com','263-322')")

conn.commit()