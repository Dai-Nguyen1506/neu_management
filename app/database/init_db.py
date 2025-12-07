import mysql.connector
import os

def run_sql_file(cursor, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        sql = f.read()

    statements = sql.split(";")
    for stmt in statements:
        stmt = stmt.strip()
        if stmt:
            cursor.execute(stmt)

def init_database():
    print("🚀 Initializing database...")

    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()

    base = "database"
    schema = os.path.join(base, "schema.sql")
    seed = os.path.join(base, "seed.sql")

    print("➡ Running schema...")
    run_sql_file(cursor, schema)

    print("➡ Running seed...")
    run_sql_file(cursor, seed)

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Database initialized successfully!")
