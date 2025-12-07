import mysql.connector

def create_local_db():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='yourpass'
    )
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS school_db")
    conn.close()
