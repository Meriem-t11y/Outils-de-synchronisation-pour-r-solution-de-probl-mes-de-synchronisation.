import threading
from ecriture_lecture import lecture, ecriture, connection_setup

connection = connection_setup()
mutex = threading.Semaphore(1)
lock_ecriture = threading.Semaphore(1)
mutex2 = threading.Semaphore(1)
nb_lecteurs = 0

def lecteur(cas):
    global nb_lecteurs
    mutex.acquire()
    nb_lecteurs += 1
    if nb_lecteurs == 1:
        lock_ecriture.acquire()
    mutex.release()

    info = lecture(connection, cas, nb_lecteurs)

    mutex.acquire()
    nb_lecteurs -= 1
    if nb_lecteurs == 0:
        lock_ecriture.release()
    mutex.release()
    return info

def redacteur(num, cas):
    mutex2.acquire()
    lock_ecriture.acquire()
    mutex2.release()

    info = ecriture(connection, num, cas)

    lock_ecriture.release()
    return info
    
