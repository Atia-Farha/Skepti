import sqlite3

# Connect to a database (or create it if it doesn't exist)
conn = sqlite3.connect("skepti.db", check_same_thread=False)
cursor = conn.cursor()

# Create a table for storing predictions
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filepath TEXT NOT NULL,
    real REAL NOT NULL,
    fake REAL NOT NULL,
    timestamp TEXT NOT NULL
)
""")

conn.commit()

from datetime import datetime

def store_prediction(filepath, real, fake):
    timestamp = datetime.now().isoformat()  # current timestamp
    cursor.execute(
        "INSERT INTO predictions (filepath, real, fake, timestamp) VALUES (?, ?, ?, ?)",
        (filepath, real, fake, timestamp)  # ✅ correct order
    )
    conn.commit()
