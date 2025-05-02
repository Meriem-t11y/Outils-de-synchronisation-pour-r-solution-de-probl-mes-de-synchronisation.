import sqlite3
from datetime import datetime
import inspect

def connection_setup():
    conn = sqlite3.connect('database.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS data (value TEXT)")
    conn.commit()
    return conn

def ecriture(conn, number, cas):
    with conn:
        conn.execute("DELETE FROM data")
        conn.execute("INSERT INTO data VALUES (?)", (str(number),))
    return [{
        "operation": inspect.currentframe().f_code.co_name,
        "cas": cas,
        "time": datetime.now().strftime("%H:%M:%S"),
        "value": number
    }]

def lecture(conn, cas, total):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    row = cursor.fetchone()
    return [{
        "operation": inspect.currentframe().f_code.co_name,
        "cas": cas,
        "time": datetime.now().strftime("%H:%M:%S"),
        "total": total,
        "value": row[0] if row else "NULL"
    }]
