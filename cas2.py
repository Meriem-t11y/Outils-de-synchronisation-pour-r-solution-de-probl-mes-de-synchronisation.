import threading
from ecriture_lecture import lecture,ecriture


mutex = threading.Semaphore(1)              # protège readcount
database_access = threading.Semaphore(1)    # accès exclusif
readcount = 0                               # nb lecteurs actifs


def lecteur(reader_id):
    global readcount
    mutex.acquire()
    readcount += 1
    if readcount == 1:
        database_access.acquire()  # le premier lecteur bloque la base
    mutex.release()
    lecture(reader_id)
    mutex.acquire()
    readcount -= 1
    if readcount == 0:
        database_access.release()  # le dernier lecteur libère la base
    mutex.release()


def redacteur(writer_id):
    database_access.acquire()  # attend que les lecteurs finissent
    ecriture(writer_id)
    database_access.release()
