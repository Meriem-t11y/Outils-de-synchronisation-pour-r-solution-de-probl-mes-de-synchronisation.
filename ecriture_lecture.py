from datetime import datetime
import sqlite3 

def connection_setup():
    connection = sqlite3.connect("lecteur_redacteur.db")
    create_table(connection)
    return connection

def create_table(connection):
    with connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS `nums` (
                `number` varchar(255)
            );""")
        
def ecriture(connection, number):
    with connection:
        cursor = connection.cursor()
        cursor.execute("""
            DELETE FROM nums
        """)
        cursor.execute("""
            INSERT INTO nums (number)
            VALUES (?)
        """, (number,))

def lecture(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM nums")
        row = cursor.fetchone()
        if row:
            return row[0]
        return None
