import threading
from datetime import datetime

mutex = threading.Semaphore(1)
lock_ecriture = threading.Semaphore(1)
mutex2 = threading.Semaphore(1)       # protège des redacteurs

global nb_lecteurs 
def lecture(reader_id):
    print(f"Lecteur {reader_id} est entrain de lire  " + datetime.now())
    #lecture mel database
    print(f"Lecteur {reader_id} a fini de lire."+ datetime.now())

def ecriture(writer_id):
    print(f"Redacteur {writer_id} est entrain d'ecrire "+datetime.now())
    #ecriture mel database
    print(f"Redacteur {writer_id} a fini d'écrire "+datetime.now())



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
