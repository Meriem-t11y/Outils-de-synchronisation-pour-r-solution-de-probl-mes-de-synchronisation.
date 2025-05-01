import threading
from datetime import datetime

mutex = threading.Semaphore(1)
lock_ecriture = threading.Semaphore(1)

def lecture(reader_id):
    print(f"Lecteur {reader_id} est entrain de lire  " + datetime.now())
    #lecture mel database
    print(f"Lecteur {reader_id} a fini de lire."+ datetime.now())

def ecriture(writer_id):
    print(f"Redacteur {writer_id} est entrain d'ecrire "+datetime.now())
    #ecriture mel database
    print(f"Redacteur {writer_id} a fini d'écrire "+datetime.now())

def lecteur(lect_id):
    global nb_lecteur
    mutex.acquire()
    nb_lecteur +=1
    if nb_lecteur==1 :
        lock_ecriture.acquire()
    mutex.release()
    lecture(lect_id)
    mutex.acquire()
    nb_lecteur-=1
    if nb_lecteur==0 :
        lock_ecriture.release()
    mutex.release()

def ecriture(ecrit_id):
    mutex.acquire()
    if(nb_lecteur==0):
        lock_ecriture.acquire()
    mutex.release()
    ecriture(ecrit_id)
    lock_ecriture.release()
