import sqlite3

conn = sqlite3.connect("chat.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM chat_data")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
