import mysql.connector
import os


def get_connection():
    """Create and return MySQL connection (Local + Railway compatible)"""

    host = os.getenv('DB_HOST', 'localhost')
    user = os.getenv('DB_USER', 'root')
    password = os.getenv('DB_PASSWORD', '')
    dbname = os.getenv('DB_NAME', 'school_db')
    port = int(os.getenv('DB_PORT', 3306))

    # Railway cần tắt SSL
    ssl_disabled = {
        "ssl_disabled": True
    }

    # 1) Tạo database nếu chưa tồn tại (chỉ cần cho Railway)
    try:
        temp_conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            **ssl_disabled
        )
        cur = temp_conn.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbname}")
        temp_conn.close()
    except Exception as e:
        print("⚠ Cannot create database:", e)

    # 2) Kết nối DB chính
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=dbname,
            port=port,
            **ssl_disabled
        )
        return conn
    except mysql.connector.Error as err:
        print("❌ Database connection error:", err)
        return None
