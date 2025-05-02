import threading
from ecriture_lecture import lecture, ecriture, connection_setup

connection = connection_setup()
mutex = threading.Semaphore(1)
read_try = threading.Semaphore(1)
database_access = threading.Semaphore(1)
readcount = 0

def lecteur(cas):
    global readcount
    read_try.acquire()
    mutex.acquire()
    readcount += 1
    if readcount == 1:
        database_access.acquire()
    mutex.release()
    read_try.release()

    value = lecture(connection, cas, readcount)

    mutex.acquire()
    readcount -= 1
    if readcount == 0:
        database_access.release()
    mutex.release()
    return value

def redacteur(num, cas):
    read_try.acquire()
    database_access.acquire()
    info = ecriture(connection, num, cas)
    database_access.release()
    read_try.release()
    return info
