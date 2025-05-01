import threading
from ecriture_lecture import lecture,ecriture

mutex = threading.Semaphore(1)
lock_ecriture = threading.Semaphore(1)
mutex2 = threading.Semaphore(1)       # protège des redacteurs

global nb_lecteurs


def lecteur(id):
    mutex2.acquire()
    mutex.acquire()
    nb_lecteurs += 1
    if nb_lecteurs == 1:
        lock_ecriture.acquire()
    mutex.release()
    mutex2.release()

    lecture(id)

    mutex.acquire()
    nb_lecteurs -= 1
    if nb_lecteurs == 0:
        lock_ecriture.release()
    mutex.release()

def redacteur(id):
    mutex2.acquire()
    lock_ecriture.acquire()
    ecriture(id)
    lock_ecriture.release()
    mutex2.release()
