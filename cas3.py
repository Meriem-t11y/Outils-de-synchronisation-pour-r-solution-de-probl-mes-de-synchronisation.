import threading
from ecriture_lecture import lecture, ecriture, connection_setup


connection = connection_setup()
# Sémaphores
mutex = threading.Semaphore(1)              # protège readcount
read_try = threading.Semaphore(1)           # priorité rédacteurs
database_access = threading.Semaphore(1)    # accès exclusif à la BDD

readcount = 0  # compteur des lecteurs

def lecteur(cas):
    global readcount
    read_try.acquire()  #p(read_try)
    mutex.acquire()    #p(mutex)
    readcount += 1
    if readcount == 1:
        database_access.acquire() #p(database_access)
    mutex.release() #v(mutex)
    read_try.release() #v(release)

    value = lecture(connection, cas, readcount)

    mutex.acquire() #p(mutex)
    readcount -= 1
    if readcount == 0:
        database_access.release()  # dernier lecteur libere la BDD
    mutex.release() #v(mutex)

    return value

def redacteur(num, cas):
    read_try.acquire()         # p(read_try)
    database_access.acquire()  # p(databse_access) pour acces exclusif

    info = ecriture(connection, num, cas)

    database_access.release()  #v(database)
    read_try.release()  #v(read_try)

    return info
