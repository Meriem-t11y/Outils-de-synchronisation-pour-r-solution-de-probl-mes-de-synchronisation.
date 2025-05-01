from datetime import datetime
import inspect
import sqlite3 

def connection_setup():
    connection = sqlite3.connect("lecteur_redacteur.db", check_same_thread=False)
    create_table(connection)
    return connection

def create_table(connection):
    with connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS `nums` (
                `number` varchar(255)
            );""")
        
def ecriture(connection, number, cas):
    with connection:
        cursor = connection.cursor()
        cursor.execute("""
            DELETE FROM nums
        """)
        cursor.execute("""
            INSERT INTO nums (number)
            VALUES (?)
        """, (number,))

    info=[{
        "operation":inspect.currentframe().f_code.co_name,
        "cas": cas,
        "time": datetime.now(),
        "value": number
    }]

    return info

def lecture(connection, cas, total):
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM nums")
        row = cursor.fetchone()
        if row:
            info=[{
                "operation":inspect.currentframe().f_code.co_name,
                "cas": cas,
                "time": datetime.now(),
                "total": total,
                "value":  row[0]
    }]
        return info
    
