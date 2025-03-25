import sqlite3
from contextlib import contextmanager

DB_NAME = "possible_ips.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS possible_ips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ambiguous_ip TEXT,
            result TEXT  -- Armazenado como string JSON
        )
    """)

    conn.commit()
    conn.close()

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    try:
        yield conn
    finally:
        conn.close()

if __name__ == "__main__":
    create_database()
    print(f"Banco de dados {DB_NAME} criado com sucesso!")