import os
from app.connection import get_connection

def run_sql_file(cursor, filename, split_by=";"):
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)
    print(f"   ... Executing {filename}")
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Tách lệnh ra trước để xử lý từng khối
        commands = content.split(split_by)

        for command in commands:
            cmd = command.strip()
            
            # --- BỘ LỌC MẠNH MẼ (Command Filter) ---
            # Bỏ qua bất kỳ lệnh nào cố tình đổi Database
            cmd_upper = cmd.upper()
            if cmd_upper.startswith("USE ") or cmd_upper.startswith("CREATE DATABASE"):
                print(f"   🚫 Skipped forbidden command in {filename}")
                continue
                
            # Bỏ qua lệnh DELIMITER (Python không cần)
            if cmd_upper.startswith("DELIMITER"):
                continue

            if cmd and not cmd.startswith("--"): 
                try:
                    cursor.execute(cmd)
                    while cursor.nextset(): pass
                except Exception as e:
                    print(f"   ⚠ Note in {filename}: {e}")

    except FileNotFoundError:
        print(f"   ❌ File not found: {filename}")

def init_database():
    conn = get_connection()
    if conn is None: return

    cursor = conn.cursor()
    print("🚀 Forcing full database initialization...")

    # Chạy theo thứ tự, tách lệnh chính xác
    run_sql_file(cursor, "schema.sql", split_by=";")
    run_sql_file(cursor, "seed.sql", split_by=";")
    run_sql_file(cursor, "views.sql", split_by=";")
    
    # Procedure và Trigger dùng $$ để tách
    run_sql_file(cursor, "procedures.sql", split_by="$$")
    run_sql_file(cursor, "triggers.sql", split_by="$$")

    conn.commit()
    cursor.close()
    conn.close()
    print("✔ Database initialized successfully.")