import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    username TEXT,
    text TEXT,
    time TEXT
)
""")

conn.commit()
conn.close()

print("Table created inside bot.db")
