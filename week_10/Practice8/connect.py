import psycopg2
from config import DB_CONFIG


def get_connection():
    """Return a new psycopg2 connection."""
    return psycopg2.connect(**DB_CONFIG)


def init_db():
    """
    Create tables and load SQL files (functions + procedures).
    Run once before using phonebook.py.
    """
    conn = get_connection()
    conn.autocommit = True
    cur = conn.cursor()

    # Tables
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id         SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name  VARCHAR(100) NOT NULL DEFAULT '',
            phone      VARCHAR(20)  NOT NULL UNIQUE
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS invalid_phones (
            id         SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name  VARCHAR(100),
            phone      VARCHAR(100),
            logged_at  TIMESTAMP DEFAULT NOW()
        );
    """)

    # Load functions.sql and procedures.sql
    for filename in ("functions.sql", "procedures.sql"):
        with open(filename, "r", encoding="utf-8") as f:
            sql = f.read()
        cur.execute(sql)
        print(f"[OK] Loaded {filename}")

    cur.close()
    conn.close()
    print("[OK] Database initialised.")


if __name__ == "__main__":
    init_db()
