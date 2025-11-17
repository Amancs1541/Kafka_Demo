import sqlite3

def get_db_connection():
    """
    Returns a SQLite database connection.
    Change this function if you want PostgreSQL/MySQL instead.
    """
    conn = sqlite3.connect("orders.db")
    conn.row_factory = sqlite3.Row
    return conn


def setup_database():
    """
    Create the orders table if it does not exist.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        item TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()
