import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE db (日本語 TEXT, English TEXT)')
print("Table created successfully")
conn.close()