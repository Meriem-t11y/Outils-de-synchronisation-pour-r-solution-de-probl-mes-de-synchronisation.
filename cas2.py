import sqlite3
import threading
from ecriture_lecture import lecture, ecriture, connection_setup 


connection = connection_setup()
mutex = threading.Semaphore(1)              # protège readcount
database_access = threading.Semaphore(1)    # accès exclusif
readcount = 0  # nb lecteurs actifs

def lecteur():
    global readcount
    mutex.acquire()
    readcount += 1
    if readcount == 1:
        database_access.acquire()  # le premier lecteur bloque la base
    mutex.release()
    value=lecture(connection)
    mutex.acquire()
    readcount -= 1
    if readcount == 0:
        database_access.release()  # le dernier lecteur libère la base
    mutex.release()

    return value


def redacteur(num):
    database_access.acquire()  # attend que les lecteurs finissent
    ecriture(connection, num)
    database_access.release()

