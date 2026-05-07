import sqlite3

DB_NAME = 'database.db'


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()


def add_alert(message):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO alerts (message) VALUES (?)',
        (message,)
    )

    conn.commit()
    conn.close()


def get_alerts():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM alerts ORDER BY created_at DESC')
    data = cursor.fetchall()

    conn.close()

    return data