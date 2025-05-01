import threading
from ecriture_lecture import lecture, ecriture, connection_setup


connection = connection_setup()
mutex = threading.Semaphore(1)
lock_ecriture = threading.Semaphore(1)
mutex2 = threading.Semaphore(1)       # protège des redacteurs

nb_lecteurs = 0

def lecteur(cas):
    mutex2.acquire()
    mutex.acquire()
    global nb_lecteurs
    nb_lecteurs += 1
    if nb_lecteurs == 1:
        lock_ecriture.acquire()
    mutex.release()
    mutex2.release()

    info=lecture(connection, cas, nb_lecteurs)

    mutex.acquire()
    nb_lecteurs -= 1
    if nb_lecteurs == 0:
        lock_ecriture.release()
    mutex.release()

    return info

def redacteur(num, cas):
    mutex2.acquire()
    lock_ecriture.acquire()

    info=ecriture(connection, num, cas)

    lock_ecriture.release()
    mutex2.release()

    return info
