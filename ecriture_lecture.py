import sqlite3
from datetime import datetime
import inspect
import time


def connection_setup():
    conn = sqlite3.connect('database.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS data (value TEXT)")
    conn.commit()
    return conn

def ecriture(conn, number, cas):
    start_time = datetime.now().strftime("%H:%M:%S.%f")[:12]
    time.sleep(5)
    with conn:
        conn.execute("DELETE FROM data")
        conn.execute("INSERT INTO data VALUES (?)", (str(number),))
    end_time = datetime.now().strftime("%H:%M:%S.%f")[:12]
    return [{
        "operation": inspect.currentframe().f_code.co_name,
        "cas": cas,
        "start_time": start_time,
        "end_time": end_time,
        "value": number
    }]

def lecture(conn, cas, total):
    start_time = datetime.now().strftime("%H:%M:%S.%f")[:12]
    time.sleep(3)  # Simulate read delay
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    row = cursor.fetchone()
    end_time = datetime.now().strftime("%H:%M:%S.%f")[:12]
    return [{
        "operation": inspect.currentframe().f_code.co_name,
        "cas": cas,
        "start_time": start_time,
        "end_time": end_time,
        "total": total,
        "value": row[0] if row else "NULL"
    }]
